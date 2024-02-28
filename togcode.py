import os.path
import numpy as np
import importlib

class Printer:
    def __init__(self, printer_profile: str):
        submodule_name = f"printers.{printer_profile}"
        submodule = importlib.import_module(submodule_name)

        # default values
        if hasattr(submodule, 'nozzle_diameter_mm'):
            self.nozzle_width = submodule.nozzle_diameter_mm
        else:
            self.nozzle_width = 0.4
        if hasattr(submodule, 'retract_mm_per_sec'):
            self.retract_speed = submodule.retract_mm_per_sec
        else:
            self.retract_speed = 45
        if hasattr(submodule, 'travel_speed_mm_per_sec'):
            self.travel_speed = submodule.travel_speed_mm_per_sec
        else:
            self.travel_speed = 120
        if hasattr(submodule, 'filament_diameter_mm'):
            self.filament_diameter = submodule.filament_diameter_mm
        else:
            self.filament_diameter = 1.75
        if hasattr(submodule, 'filament_priming_mm'):
            self.filament_priming = submodule.filament_priming_mm
        else:
            self.filament_priming = 0.4
        if hasattr(submodule, 'z_lift_mm'):
            self.z_lift = submodule.z_lift_mm
        else:
            self.z_lift = 0.4
        if hasattr(submodule, 'filament_density'):
            self.filament_density = submodule.filament_density
        else:
            self.filament_density = 1.25
        self.print_speed = 30
        self.first_layer_speed = 15
        self.flow_multiplier = 1
        self.bed_temp = 55
        self.extruder_temp = 190
        self.layer_height = 0.08
        self.origin_is_bed_center = False
        self.nrows = 1
        self.ncols = 1
        self.nloops = 5
        self.rectangle_distance = 3

        # constants
        self.z_lift_speed = 10
        self.travel_max_length_without_retract = 2
        self.linear_advance_factor = 30

        # coordinates
        self.bed_size = np.array([submodule.bed_size_x_mm, submodule.bed_size_y_mm])

        if hasattr(submodule, 'bed_circular') and submodule.bed_circular:
            self.origin = np.array([0, 0])
        else:
            self.origin = self.bed_size / 2.0

        # useful data
        self.total_extrusion_length = 0
        self.total_print_dist = 0
        self.total_travel_dist = 0

        # gcode templates
        self.header = ""
        self.footer = ""
        self.load_gcode_templates(printer_profile)

    def get_print_feedrate(self) -> int:
        # mm/s to mm/min
        return int(self.print_speed * 60)

    def get_first_layer_feedrate(self) -> int:
        # mm/s to mm/min
        return int(self.first_layer_speed * 60)

    def get_travel_feedrate(self) -> int:
        # mm/s to mm/min
        return int(self.travel_speed * 60)

    def get_retract_feedrate(self) -> int:
        # mm/s to mm/min
        return int(self.retract_speed * 60)

    def get_z_lift_feedrate(self) -> int:
        # mm/s to mm/min
        return int(self.retract_speed * 60)

    def update_extrusion_length(self, local_length: float):
        self.total_extrusion_length += self.compute_extrusion_length(local_length)

    def to_gcode(self, trajectories, filename="output.gcode"):
        trajectories = Printer.center_trajectories(trajectories)
        trajectories = self.duplicate(trajectories)
        trajectories = self.rectangle(trajectories) + trajectories

        self.write_gcode(trajectories, filename)

        self.print_estimations()

    def write_gcode(self, trajectories, filename="output.gcode"):
        with open(filename, "w", encoding="utf-8") as f:
            # Write header
            f.write(self.header)

            center = np.array([self.origin[0], self.origin[1], 0])
            prev_point = None
            for trajectory in trajectories:
                if prev_point is None:
                    f.write(self.travel_to(trajectory[0, :] + center))
                else:
                    f.write(self.travel(prev_point, trajectory[0, :] + center))
                    dist = np.linalg.norm(trajectory[0, :] + center - prev_point)
                    self.total_travel_dist += dist

                    # detect layer height change
                    if trajectory[0, 2] - prev_point[2] > 1e-5:
                        self.layer_height = trajectory[0, 2] - prev_point[2]
                prev_point = trajectory[0, :] + center

                for point in trajectory:
                    point += center
                    dist = np.linalg.norm(point - prev_point)
                    self.total_print_dist += dist
                    self.update_extrusion_length(dist)

                    if point[2] <= self.layer_height:
                        f.write(
                            f"G1 F{self.get_first_layer_feedrate()} X{point[0]:.3f} Y{point[1]:.3f} Z{point[2]:.4f} E{self.total_extrusion_length:.5f}\n"
                        )
                    else:
                        f.write(
                            f"G1 F{self.get_print_feedrate()} X{point[0]:.3f} Y{point[1]:.3f} Z{point[2]:.4f} E{self.total_extrusion_length:.5f}\n"
                        )
                    prev_point = point

            # Write footer
            f.write(self.footer)

    def travel(self, point_start: np.ndarray, point_end: np.ndarray) -> str:
        dist = np.linalg.norm(point_end - point_start)

        travel_str = ""
        if dist < self.travel_max_length_without_retract:
            travel_str += ";travel\n"
            travel_str += f"G0 F{self.get_travel_feedrate()} X{point_end[0]:.3f} Y{point_end[1]:.3f} Z{point_end[2]:.2f}\n"
        else:
            point_z_lifted = max(point_end[2], point_start[2]) + self.z_lift

            direction = (point_end - point_start) / dist
            intermediate1 = point_start + self.z_lift * direction
            intermediate2 = point_end - self.z_lift * direction

            # Retract
            travel_str += ";retract\n"
            self.total_extrusion_length -= self.filament_priming
            travel_str += f"G1 F{self.get_retract_feedrate()} E{self.total_extrusion_length:.5f}\n"
            # Travel
            travel_str += ";travel\n"
            travel_str += f"G0 F{self.get_z_lift_feedrate()} X{intermediate1[0]:.3f} Y{intermediate1[1]:.3f} Z{point_z_lifted:.2f}\n"
            travel_str += f"G0 F{self.get_travel_feedrate()} X{intermediate2[0]:.3f} Y{intermediate2[1]:.3f} Z{point_z_lifted:.2f}\n"
            travel_str += f"G0 F{self.get_z_lift_feedrate()} X{point_end[0]:.3f} Y{point_end[1]:.3f} Z{point_end[2]:.2f}\n"
            # Prime
            travel_str += ";prime\n"
            self.total_extrusion_length += self.filament_priming
            travel_str += f"G1 F{self.get_retract_feedrate()} E{self.total_extrusion_length:.5f}\n"
        return travel_str

    def travel_to(self, point_end: np.ndarray) -> str:
        # Retract
        travel_str = ";retract\n"
        self.total_extrusion_length -= self.filament_priming
        travel_str += (
            f"G1 F{self.get_retract_feedrate()} E{self.total_extrusion_length:.5f}\n"
        )
        # Travel
        travel_str += ";travel\n"
        travel_str += f"G0 F{self.get_travel_feedrate()} X{point_end[0]:.3f} Y{point_end[1]:.3f} Z{point_end[2] + self.z_lift:.2f}\n"
        travel_str += f"G0 F{self.get_z_lift_feedrate()} X{point_end[0]:.3f} Y{point_end[1]:.3f} Z{point_end[2]:.2f}\n"

        # Prime
        travel_str += ";prime\n"
        self.total_extrusion_length += self.filament_priming
        travel_str += (
            f"G1 F{self.get_retract_feedrate()} E{self.total_extrusion_length:.5f}\n"
        )
        return travel_str

    def print_estimations(self):
        print(f"Total length = {self.total_extrusion_length / 1000:.2f}m")
        print(
            f"Weight estimation = {self.total_extrusion_length * self.filament_density / 1000:.2f}g"
        )
        t = (
            self.total_print_dist / self.print_speed
            + self.total_travel_dist / self.travel_speed
        ) / 60
        print(f"Rough time estimation = {t // 60:.0f} hours {t % 60:.0f} minutes")

    def load_gcode_templates(self, printer_profile: str):
        # Get the printer profile header and footer
        source_folder = os.path.dirname(__file__)
        printer_profile_header_path = f"{source_folder}/printers/{printer_profile}/header.gcode"
        printer_profile_footer_path = f"{source_folder}/printers/{printer_profile}/footer.gcode"

        # File to string
        with open(printer_profile_header_path, "r") as f:
            header = f.read()
        with open(printer_profile_footer_path, "r") as f:
            footer = f.read()

        # Put user defined parameters in the header
        header = header.replace("<HBPTEMP>", str(int(self.bed_temp)))
        header = header.replace("<TOOLTEMP>", str(int(self.extruder_temp)))
        # G29 ; auto bed levelling\nG0 F6200 X0 Y0 ; back to the origin to begin the purge
        header = header.replace("<BEDLVL>", "G0 F6200 X0 Y0")
        header = header.replace("<NOZZLE_DIAMETER>", str(self.nozzle_width))

    # add rectangle around object
    def rectangle(self, trajectories):
        dimensions_plus_margin = (
            Printer.bounding_box(trajectories)
            + self.rectangle_distance
            + 2 * self.nloops * self.nozzle_width
        )

        rect_trajectories = []

        for i in range(self.nloops):
            rect_trajectory = []
            X = dimensions_plus_margin[0] / 2 - self.nozzle_width * i
            Y = dimensions_plus_margin[1] / 2 - self.nozzle_width * i
            rect_trajectory.append([-X, -Y, self.layer_height])
            rect_trajectory.append([+X, -Y, self.layer_height])
            rect_trajectory.append([+X, +Y, self.layer_height])
            rect_trajectory.append([-X, +Y, self.layer_height])
            rect_trajectory.append([-X, -Y, self.layer_height])
            rect_trajectories.append(np.array(rect_trajectory))

        return rect_trajectories

    def compute_extrusion_length(self, local_length: float) -> float:
        """Compute the length of the filament to extrude.

        Notes
        -----
        https://3dprinting.stackexchange.com/questions/6289/how-is-the-e-argument-calculated-for-a-given-g1-command
        """
        crsec = np.pi * self.filament_diameter**2 / 4.0
        v_mm3 = local_length * self.layer_height * self.nozzle_width
        return self.flow_multiplier * v_mm3 / crsec

    def center_trajectories(trajectories):
        avg = np.array([0.0, 0.0, 0.0])
        count = 0
        for trajectory in trajectories:
            for point in trajectory:
                avg += point
                count += 1
        avg = avg / count
        avg[2] = 0

        for trajectory in trajectories:
            trajectory -= avg

        return trajectories

    def bounding_box(trajectories):
        object_max_xy = np.array([0, 0, 0])
        object_min_xy = np.array([0, 0, 0])
        for trajectory in trajectories:
            object_max_xy = np.maximum(np.amax(trajectory, axis=0), object_max_xy)
            object_min_xy = np.minimum(np.amin(trajectory, axis=0), object_min_xy)

        return object_max_xy[:2] - object_min_xy[:2]

    def duplicate(self, input_traj):
        if self.nrows * self.ncols <= 1:
            return input_traj

        dimensions_plus_margin = Printer.bounding_box(input_traj) + 5

        trajectories = []
        for i in range(self.ncols):
            for j in range(self.nrows):
                centerX = (i - (self.ncols - 1) / 2) * dimensions_plus_margin[0]
                centerY = (j - (self.nrows - 1) / 2) * dimensions_plus_margin[1]
                for trajectory in input_traj:
                    trajectories.append(trajectory + np.array([centerX, centerY, 0]))
        return trajectories


def read_trajectories(filename):
    print("reading file " + filename)

    with open(filename, "r") as file:
        paths = []
        line = file.readline()
        while line:
            num_vertices = int(line)
            path = []
            for i in range(num_vertices):
                line = file.readline()
                vertex = line.split()
                path.append([float(x) for x in vertex])
            paths.append(np.array(path))
            line = file.readline()
    return paths


def export_gcode(
    trajectories,
    printer_profile: str,
    output_filename="output.gcode",
    nozzle_width=None,
    retract_speed=None,
    travel_speed=None,
    filament_diameter=None,
    filament_priming=None,
    z_lift=None,
    print_speed=None,
    first_layer_speed=None,
    flow_multiplier=None,
    bed_temp=None,
    extruder_temp=None,
    layer_height=None,
    nrows=None,
    ncols=None,
):

    printer = Printer(printer_profile)

    printer.nozzle_width = nozzle_width or printer.nozzle_width
    printer.retract_speed = retract_speed or printer.retract_speed
    printer.travel_speed = travel_speed or printer.travel_speed
    printer.filament_diameter = filament_diameter or printer.filament_diameter
    printer.filament_priming = filament_priming or printer.filament_priming
    printer.z_lift = z_lift or printer.z_lift
    printer.print_speed = print_speed or printer.print_speed
    printer.first_layer_speed = first_layer_speed or printer.first_layer_speed
    printer.flow_multiplier = flow_multiplier or printer.flow_multiplier
    printer.bed_temp = bed_temp or printer.bed_temp
    printer.extruder_temp = extruder_temp or printer.extruder_temp
    printer.layer_height = layer_height or printer.layer_height
    printer.nrows = nrows or printer.nrows
    printer.ncols = ncols or printer.ncols

    printer.to_gcode(trajectories, output_filename)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert the cycle generated by fill_2d_shape.py to machine instructions. Input: The JSON file used by fill_2d_shape.py. Output: The G-code to print the generated cycle."
    )
    parser.add_argument("input_filename", help="File containing the trajectory data")
    parser.add_argument("printer_profile", help="The printer profile.")
    parser.add_argument(
        "-o", "--output", help="Name of the output gcode file", default="output.gcode"
    )
    parser.add_argument(
        "-nw",
        "--nozzle_width",
        help="The nozzle diameter in millimeter. Default: 0.4mm.",
        type=float,
    )
    parser.add_argument(
        "-s",
        "--print_speed",
        help="The speed of the moving head, in mm/s. Default: 30mm/s.",
        type=float,
    )
    parser.add_argument(
        "-rs",
        "--retract_speed",
        help="Speed of retraction. Default: 45mm/s.",
        type=float,
    )
    parser.add_argument(
        "-fs",
        "--first_layer_speed",
        help="Speed of the moving head for the first layer, in mm/s. Default: 30mm/s.",
        type=float,
    )
    parser.add_argument(
        "-ts",
        "--travel_speed",
        help="Travel speed in mm/s. Default: 120mm/s.",
        type=float,
    )
    parser.add_argument(
        "-fm", "--flow_multiplier", help="Flow multiplier. Default: 1", type=float
    )
    parser.add_argument(
        "-bt",
        "--bed_temp",
        help="Bed temperature in degrees Celsius. Default: 55.",
        type=int,
    )
    parser.add_argument(
        "-et",
        "--extruder_temp",
        help="Extruder temperature in degree Celsius. Default: 190.",
        type=int,
    )
    parser.add_argument(
        "-lh",
        "--layer_height",
        help="Layer height. Default: the layer height associated with the polyline. Default: 0.08mm",
        type=float,
    )
    parser.add_argument(
        "-fd",
        "--filament_diameter",
        help="Filament diameter used by the printer. Default: 1.75 mm.",
        type=float,
    )
    parser.add_argument(
        "-fp",
        "--filament_priming",
        help="Retraction setting. Between 0.4mm and 0.8mm of retract/prime for direct-drive setup, between 3mm and 6mm for bowden (stock) setup. Default: 0.4 mm.",
        type=float,
    )
    parser.add_argument(
        "-zl",
        "--z_lift",
        help="Distance to move the print head up (or the build plate down) after each retraction, right before a travel move takes place. Default: 0.4",
        type=float,
    )
    parser.add_argument(
        "--ncols", help="Object count along the x-axis. Default: 1.", type=int
    )
    parser.add_argument(
        "--nrows", help="Object count along the y-axis. Default: 1.", type=int
    )

    args = parser.parse_args()
    printer = Printer(args.printer_profile)

    printer.nozzle_width = args.nozzle_width or printer.nozzle_width
    printer.retract_speed = args.retract_speed or printer.retract_speed
    printer.travel_speed = args.travel_speed or printer.travel_speed
    printer.filament_diameter = args.filament_diameter or printer.filament_diameter
    printer.filament_priming = args.filament_priming or printer.filament_priming
    printer.z_lift = args.z_lift or printer.z_lift
    printer.print_speed = args.print_speed or printer.print_speed
    printer.first_layer_speed = args.first_layer_speed or printer.first_layer_speed
    printer.flow_multiplier = args.flow_multiplier or printer.flow_multiplier
    printer.bed_temp = args.bed_temp or printer.bed_temp
    printer.extruder_temp = args.extruder_temp or printer.extruder_temp
    printer.layer_height = args.layer_height or printer.layer_height
    printer.nrows = args.nrows or printer.nrows
    printer.ncols = args.ncols or printer.ncols

    trajectories = read_trajectories(args.input_filename)
    printer.to_gcode(trajectories, args.output)
