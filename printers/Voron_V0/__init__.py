# Voron V0 Profile
# Hugron Pierre-Alexandre 29/06/2021
# Updated by Bedell Pierre 05/10/2022

# Custom checkox to use a direct-drive extruder (for most V0.1)
#add_checkbox_setting('direct_drive', 'Extruder in direct-drive',"Use proper retraction distances for a direct-drive extruder (for most V0.1)")
direct_drive = False

##################################################

# Build Area dimensions
bed_size_x_mm = 120
bed_size_y_mm = 120
bed_size_z_mm = 120

# Printer Extruder
extruder_count = 1
nozzle_diameter_mm = 0.4
filament_diameter_mm = 1.75

# Layer height limits
z_layer_height_mm_min = nozzle_diameter_mm * 0.10
z_layer_height_mm_max = nozzle_diameter_mm * 0.80

# Retraction Settings
# between 0.5mm and 0.8mm of retract/prime for direct-drive setup (V0.1), 
# between 1mm and 3mm for bowden (V0) setup
if direct_drive:
  filament_priming_mm = 0.4 
else:
  filament_priming_mm = 2.0

priming_mm_per_sec = 30
retract_mm_per_sec = 50

# Printing temperatures limits
extruder_temp_degree_c = 210
extruder_temp_degree_c_min = 150
extruder_temp_degree_c_max = 290

bed_temp_degree_c = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 120

# Printing speed limits
print_speed_mm_per_sec = 120
print_speed_mm_per_sec_min = 5
print_speed_mm_per_sec_max = 400

perimeter_print_speed_mm_per_sec = 60
perimeter_print_speed_mm_per_sec_min = 5
perimeter_print_speed_mm_per_sec_max = 400

cover_print_speed_mm_per_sec = 120
cover_print_speed_mm_per_sec_min = 5
cover_print_speed_mm_per_sec_max = 400

first_layer_print_speed_mm_per_sec = 40
first_layer_print_speed_mm_per_sec_min = 5
first_layer_print_speed_mm_per_sec_max = 100

travel_speed_mm_per_sec = 200
travel_speed_mm_per_sec_min = 20
travel_speed_mm_per_sec_max = 500

# Acceleration settings
# max settings are provided for reference only, as they should remain as set up on the machine
# x_max_speed = 500 # mm/s
# y_max_speed = 500 # mm/s
# z_max_speed = 20 # mm/s
# e_max_speed = 30 # mm/s

# x_max_acc = 20000 # mm/s²
# y_max_acc = 20000 # mm/s²
# z_max_acc = 500 # mm/s²
# e_max_acc = 5000 # mm/s²

default_acc = 8500 # mm/s²
#e_prime_max_acc = 5000 # mm/s²
perimeter_acc = 5000 # mm/s²
infill_acc = 8500 # mm/s²
first_layer_acc = 2000 # mm/s²

# default_jerk = 9 # mm/s

# Misc default settings
add_brim = True
brim_distance_to_print_mm = 2.0
brim_num_contours = 3

enable_z_lift = True
z_lift_mm = 0.4

# default filament infos (when using "custom" profile)
name_en = "PLA"
filament_density = 1.25 #g/cm3 PLA
