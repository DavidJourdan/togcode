; preheating the bed
M140 S<HBPTEMP> ; starting to heat the bed
M150 ; temperature report

; preheating the chamber
M141 S<HBPTEMP> ; starting to heat the chamber
M150 ; temperature report

; preheating the extruder(s)
M104 T0 S<TOOLTEMP>
M150 ; temperature report

; preparing the machine
M82 ; absolute extrusion mode
G90 ; absolute positionning
G28 ; home all axis
M375 ; load previous mesh / bed level

; waiting for target temperatures to be reached
M190 S<HBPTEMP>
M150 ; temperature report
M109 T0 S<TOOLTEMP>
M150 ; temperature report
