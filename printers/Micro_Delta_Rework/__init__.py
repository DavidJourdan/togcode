# EmotionTech Micro Delta Rework
# Pierre Bedell 05/06/2018

# Build Area dimensions
bed_circular  = True
bed_radius = 75.0

bed_size_x_mm = bed_radius * 2
bed_size_y_mm = bed_radius * 2

bed_size_z_mm = 200

# Printer Extruder
extruder_count = 1
nozzle_diameter_mm = 0.4
filament_diameter_mm = 1.75

# Layer height limits
z_layer_height_mm_min = nozzle_diameter_mm * 0.15
z_layer_height_mm_max = nozzle_diameter_mm * 0.75

# Retraction Settings
filament_priming_mm = 4.5 # min 0.5 - max 4
priming_mm_per_sec = 30
retract_mm_per_sec = 30

# Printing temperatures limits
extruder_temp_degree_c = 210
extruder_temp_degree_c_min = 150
extruder_temp_degree_c_max = 270

bed_temp_degree_c = 50
bed_temp_degree_c_min = 0
bed_temp_degree_c_max = 110

# Printing speed limits
print_speed_mm_per_sec = 60
print_speed_mm_per_sec_min = 10
print_speed_mm_per_sec_max = 200

perimeter_print_speed_mm_per_sec = 40
perimeter_print_speed_mm_per_sec_min = 20
perimeter_print_speed_mm_per_sec_max = 200

cover_print_speed_mm_per_sec = 40
cover_print_speed_mm_per_sec_min = 20
cover_print_speed_mm_per_sec_max = 200

first_layer_print_speed_mm_per_sec = 20
first_layer_print_speed_mm_per_sec_min = 5
first_layer_print_speed_mm_per_sec_max = 50

travel_speed_mm_per_sec = 100

 