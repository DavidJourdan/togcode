# EmotionTech Strateo3D profile
# Bedell Pierre 21/07/2020

# Machine runing on Smoothieware
# for specific Gcodes to use, refer to the documentation here: https://smoothieware.org/supported-g-codes

# #####################
# Build Area dimensions
# #####################
bed_size_x_mm = 600
bed_size_y_mm = 420
bed_size_z_mm = 495

# #################
# Printer Extruders
# #################
# Note: Extruder 0 is on the right, Extruder 1 is on the left
extruder_count = 2
nozzle_diameter_mm = 0.6
filament_diameter_mm = 1.75

# ###################
# Retraction Settings
# ###################
filament_priming_mm = 0.8
retract_mm_per_sec = 25
priming_mm_per_sec = 20

# ###################
# Layer height limits
# ###################
z_layer_height_mm = 0.3
z_layer_height_mm_min = nozzle_diameter_mm * 0.125
z_layer_height_mm_max = nozzle_diameter_mm * 0.8

# ############################
# Printing temperatures limits
# ############################
extruder_temp_degree_c = 200
extruder_temp_degree_c_min = 150
extruder_temp_degree_c_max = 270

bed_temp_degree_c = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 110

chamber_temp_degree_c = 0
chamber_temp_degree_c_min = 0
chamber_temp_degree_c_max = 110

# #####################
# Printing speed limits
# #####################
print_speed_mm_per_sec = 40
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 100

perimeter_print_speed_mm_per_sec = 30
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 80

cover_print_speed_mm_per_sec = 30
cover_print_speed_mm_per_sec_min = 5
cover_print_speed_mm_per_sec_max = 80

first_layer_print_speed_mm_per_sec = 25
first_layer_print_speed_mm_per_sec_min = 5
first_layer_print_speed_mm_per_sec_max = 30

travel_speed_mm_per_sec = 100
travel_speed_mm_per_sec_min = 60
travel_speed_mm_per_sec_max = 200

default_acc = 1500 # mm/s²
perimeter_acc = 1000 # mm/s²
infill_acc = 1500 # mm/s²
travel_acc = 1500 # mm/s²

default_junction_deviation = 0.01 # mm/s
perimeter_junction_deviation = 0.001 # mm/s
infill_junction_deviation = 0.01 # mm/s
travel_junction_deviation = 0.01 # mm/s

# #############
# Misc settings
# #############
# Purge Tower
gen_tower = False
tower_side_x_mm = 10.0
tower_side_y_mm = 5.0
tower_brim_num_contours = 12

# extruder swap behaviour
enable_active_temperature_control = True
extruder_swap_zlift_mm = 0.2
extruder_swap_retract_length_mm = 6.5
extruder_swap_retract_speed_mm_per_sec = 25.0

# brim
add_brim = True
brim_distance_to_print_mm = 1.0
brim_num_contours = 3

# z-hop
enable_z_lift = True
z_lift_mm = 0.4

# misc
process_thin_features = False
