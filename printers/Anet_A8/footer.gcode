; End GCode
M104 S0 ; extruder heater off
M140 S0 ; heated bed heater off
M106 S0 ; turn fan off
G91 ; relative positioning
G1 E-5 F300 ; retract the filament a bit before lifting the nozzle
G1 Z+0.5 E-5 F3600 ; move Z up a bit and retract filament even more
G28 X0 Y0 ; Home X and Y
G0 F6200 Y150 ; build plate moved forward to present the printed part
G90 ; absolute positioning
G92 E0 ; 
M84 ; steppers off
