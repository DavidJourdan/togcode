# Flsun SR Profile
# Hardy Damien 14/01/2022
# Based on Wasp 2040 Pro Profile

# Build Area dimensions
bed_radius = 132
bed_circular = True

bed_size_x_mm = bed_radius * 2
bed_size_y_mm = bed_radius * 2

bed_size_z_mm = 320

# Printer Extruder
extruder_count = 1
nozzle_diameter_mm = 0.4
filament_diameter_mm = 1.75

# Layer height limits
z_layer_height_mm_min = nozzle_diameter_mm * 0.25
z_layer_height_mm_max = nozzle_diameter_mm * 0.75

# Retraction Settings
filament_priming_mm = 6.5 # default cura
priming_mm_per_sec = 40 # default cura
retract_mm_per_sec = 40 # default cura

# Printing temperatures limits
extruder_temp_degree_c = 220
extruder_temp_degree_c_min = 190 # most likely will not work below that value
extruder_temp_degree_c_max = 250 # bowden ptfe

bed_temp_degree_c = 60
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 100

# Printing speed limits
print_speed_mm_per_sec = 150
print_speed_mm_per_sec_min = 10
print_speed_mm_per_sec_max = 250 # HW limit at 200 with motors not tested yet

perimeter_print_speed_mm_per_sec = 75 #outer-wall ??
perimeter_print_speed_mm_per_sec_min = 10
perimeter_print_speed_mm_per_sec_max = 200

cover_print_speed_mm_per_sec = 70 # skin ?
cover_print_speed_mm_per_sec_min = 10
cover_print_speed_mm_per_sec_max = 200

first_layer_print_speed_mm_per_sec = 35
first_layer_print_speed_mm_per_sec_min = 10
first_layer_print_speed_mm_per_sec_max = 150

travel_speed_mm_per_sec = 180
travel_speed_mm_per_sec_min = 50
travel_speed_mm_per_sec_max = 800

#DH based on cura
support_print_speed_mm_per_sec = 80

# Misc default settings
add_brim = True
brim_distance_to_print_mm = 1.0
brim_num_contours = 4
z_lift_mm = 0.6

process_thin_features = False
