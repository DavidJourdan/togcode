G21 ; set units to millimeters
M82 ; use absolute distances for extrusion
G90 ; use absolute coordinates
M117 ; Homing X/Y ...
G28 X0 Y0
M117 ; Homing Z ...
G28 Z0
M117 ; Start heating bed ...
M190 S<HBPTEMP> ; wait for bed temperature to be reached
M117 Start heating ...
M104 S<TOOLTEMP> ; set temperature
M117 ; Heating ...
M109 S<TOOLTEMP> ; wait for temperature to be reached
M117 ; Purge line ...
G92 E0
G1 Z1.0 F3000 ; move z up little to prevent scratching of surface
G1 X20 Y10 Z0.3 F5000.0 ; move to start-line position
G1 X150 Y10 Z0.3 F1500.0 E15 ; draw 1st line
G1 X150 Y10 Z0.3 F5000.0 ; move to side a little
G1 X20 Y10.3 Z0.3 F1500.0 E30 ; draw 2nd line
G92 E0 ; reset extruder
; done purging extruder
M117 ; Printing ...
