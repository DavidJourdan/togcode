# Ultimaker S3
# Sylvain Lefebvre  2017-07-28

# Build Area dimensions
bed_size_x_mm = 230 # 233 (max build width) - extruder 1 offset (18)
bed_size_y_mm = 190
bed_size_z_mm = 200

# Extruders default settings
extruder_count = 2
filament_diameter_mm = 2.85
# default nozzle diameter
nozzle_diameter_mm = 0.4
# specific nozzle diameter (for different printcore use)
# nozzle and printcore management will be added in a future release
nozzle_diameter_mm_0 = 0.4 # extruder 0
nozzle_diameter_mm_1 = 0.4 # extruder 1

# Retraction settings
filament_priming_mm = 6.50
priming_mm_per_sec = 40
retract_mm_per_sec = 40

# Layer height limits
z_layer_height_mm = 0.2

# Printing temperatures limits
extruder_temp_degree_c = 210
extruder_temp_degree_c_min = 150
extruder_temp_degree_c_max = 300

bed_temp_degree_c     = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 120

# Printing speed limits
print_speed_mm_per_sec = 40
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 150

perimeter_print_speed_mm_per_sec = 30
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 80

cover_print_speed_mm_per_sec = 30
cover_print_speed_mm_per_sec_min = 5
cover_print_speed_mm_per_sec_max = 80

first_layer_print_speed_mm_per_sec = 20
first_layer_print_speed_mm_per_sec_min = 1
first_layer_print_speed_mm_per_sec_max = 50

travel_speed_mm_per_sec = 150

# Purge Tower
gen_tower = False
tower_side_x_mm = 10.0
tower_side_y_mm = 5.0
tower_brim_num_contours = 12

tower_at_location = True # Requires extruder to swap material at a given location,
                         # this also forces the tower to appear at this same location.
tower_location_x_mm = 201
tower_location_y_mm = 179

extruder_swap_retract_length_mm = 16.0
extruder_swap_retract_speed_mm_per_sec = 30.0

enable_active_temperature_control = True

# Misc Settings
add_brim = True
brim_distance_to_print_mm = 2.0
brim_num_contours = 2

add_raft = False
raft_spacing = 1.0

gen_supports = False
support_extruder = 0

enable_z_lift = True
z_lift_mm = 0.4