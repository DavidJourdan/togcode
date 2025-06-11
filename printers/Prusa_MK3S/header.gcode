M201 X1000 Y1000 Z200 E5000 ; sets maximum accelerations, mm/sec^2
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec
M204 S1250 T1250 ; sets acceleration (S) and retract acceleration (R), mm/sec^2
M205 X8 Y8 Z0.4 E4.5 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec

M862.3 P "MK3S" ; printer model check
M862.1 P<NOZZLE_DIAMETER> ; nozzle diameter check
M115 U3.13.2 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode

M104 S<TOOLTEMP> ; set extruder temp
M140 S<HBPTEMP> ; set bed temp
M190 S<HBPTEMP> ; wait for bed temp
M109 S<TOOLTEMP> ; wait for extruder temp
M107

G28 W ; home all without mesh bed level
G80 ; mesh bed leveling
G90 ; use absolute coordinates

G1 Z0.2 F720
G1 Y-3 F1000 ; go outside print area
G92 E0
G1 X60 E9 F1000 ; intro line
G1 X100 E12.5 F1000 ; intro line

G92 E0
M221 S95

; Don't change E values below. Excessive value can damage the printer.

G21 ; set units to millimeters
G90 ; use absolute coordinates
M82  ; extruder absolute mode
M900 K0.04 ; Filament gcode LA 1.5
M900 K18 ; Filament gcode LA 1.0

G92 E0.0
