# E3D Toolchanger
# Hugron Pierre-Alexandre  2021-09-21

# Build Area dimensions
bed_size_x_mm = 300
bed_size_y_mm = 200
bed_size_z_mm = 280

# Extruders default settings
extruder_count = 4
filament_diameter_mm = 1.75
# specific nozzle diameter
nozzle_diameter_mm_0 = 0.4 # extruder T0 E3D Hemera direct drive
nozzle_diameter_mm_1 = 0.4 # extruder T1 E3D Hemera direct drive
nozzle_diameter_mm_2 = 0.4 # extruder T2 E3D Hemera direct drive
nozzle_diameter_mm_3 = 0.4 # extruder T3 E3D Hemera direct drive

# Retraction settings
filament_priming_mm = 0.4 # 0.4mm for hemera, 4mm for bowden setup(not tested value)
priming_mm_per_sec = 30
retract_mm_per_sec = 50
extruder_swap_retract_mm = filament_priming_mm*2

# Layer height limits
z_layer_height_mm = 0.2

# Printing temperatures limits
extruder_temp_degree_c = 210
extruder_temp_degree_c_min = 170
extruder_temp_degree_c_max = 280

bed_temp_degree_c     = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 120

# Printing speed limits
print_speed_mm_per_sec = 100
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 200

perimeter_print_speed_mm_per_sec = 50
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 200

cover_print_speed_mm_per_sec = 60
cover_print_speed_mm_per_sec_min = 5
cover_print_speed_mm_per_sec_max = 200

first_layer_print_speed_mm_per_sec = 20
first_layer_print_speed_mm_per_sec_min = 1
first_layer_print_speed_mm_per_sec_max = 50

travel_speed_mm_per_sec = 200

print_speed_microlayers_mm_per_sec = 40
mixing_shield_speed_multiplier = 1

# Purge Tower
gen_tower = True
tower_side_x_mm = 20.0
tower_side_y_mm = 20.0
tower_brim_num_contours = 8

tower_at_location = True # Requires extruder to swap material at a given location,
                          # this also forces the tower to appear at this same location.
tower_location_x_mm = 280
tower_location_y_mm = 180

extruder_swap_retract_length_mm = 1.0
extruder_swap_retract_speed_mm_per_sec = 50.0
enable_active_temperature_control = True

# Misc Settings
add_brim = True
brim_distance_to_print_mm = 2.0
brim_num_contours = 3

add_raft = False
raft_spacing = 1.0

gen_supports = False
support_extruder = 0

travel_straight = True
enable_z_lift = True
z_lift_mm = 0.4

travel_max_length_without_retract = 1
extruder_swap_zlift_mm = 0.4

flow_dampener_path_length_start_mm = 1
flow_dampener_path_length_end_mm = 1
flow_dampener_e_length_mm = 3

extruder_mix_count = 1
