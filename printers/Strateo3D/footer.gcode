; turning off extruder(s) heaters
M104 T0 S0

M140 S0 ; turning off bed
M141 S0 ; turning off chamber

; moving toolhead back to origin
G91 ; switch to relative positioning
G0 Z1 ; move the tool head up for clearance
G90 ; switch back to absolute positioning
G28

M801.0
M192

M84 ; disable motors
M82 ; absolute extrusion mode

;End of Gcode