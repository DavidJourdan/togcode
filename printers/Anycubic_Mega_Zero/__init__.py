# Anyucubic Mega Zero Profile
# Bedell Pierre 25/06/2021

# Build Area dimensions
bed_size_x_mm = 220
bed_size_y_mm = 220
bed_size_z_mm = 250

# Printer Extruder
extruder_count = 1
nozzle_diameter_mm = 0.4
filament_diameter_mm = 1.75

# Layer height limits
z_layer_height_mm_min = nozzle_diameter_mm * 0.10
z_layer_height_mm_max = nozzle_diameter_mm * 0.75

# Retraction Settings
filament_priming_mm = 7.0
priming_mm_per_sec = 30
retract_mm_per_sec = 30

# Printing temperatures limits
extruder_temp_degree_c = 200
extruder_temp_degree_c_min = 150
extruder_temp_degree_c_max = 270

bed_temp_degree_c = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 120

# Printing speed limits
print_speed_mm_per_sec = 40
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 200

perimeter_print_speed_mm_per_sec = 30
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 200

cover_print_speed_mm_per_sec = 30
cover_print_speed_mm_per_sec_min = 5
cover_print_speed_mm_per_sec_max = 200

first_layer_print_speed_mm_per_sec = 20
first_layer_print_speed_mm_per_sec_min = 5
first_layer_print_speed_mm_per_sec_max = 50

travel_speed_mm_per_sec = 100

# Misc default settings
add_brim = True
brim_distance_to_print_mm = 1.0
brim_num_contours = 4
z_lift_mm = 0.6

process_thin_features = False
