reset
set angles radians
set terminal pngcairo size 800,400
set output "images/functions.png"

set samples 1000
set xrange [0:2*pi]
set yrange [-1:5]

z0 = 5

set object 1 rectangle from 0, graph 0 to pi/2, graph 1 \
    fc rgb "blue" fillstyle solid 0.1 behind
set object 3 rectangle from pi, graph 0 to 3*pi/2, graph 1 \
    fc rgb "blue" fillstyle solid 0.1 behind

set object 2 rectangle from pi/2, graph 0 to 3*pi/2, graph 1 \
    fc rgb "green" fillstyle solid 0.1 behind
set object 4 rectangle from 3*pi/2, graph 0 to 2*pi, graph 1 \
    fc rgb "green" fillstyle solid 0.1 behind

set label 1 "z0" at z0,0 point pt 7 offset -1,-1
set label 2 "pi/2" at pi/2,0 point pt 7 offset -5,1
set label 3 "pi" at pi,0 point pt 7 offset -5,1
set label 4 "3pi/2" at 3*pi/2,0 point pt 7 offset -5,1
set label 5 "2pi" at 2*pi,0 point pt 7 offset -5,1

plot 0 lc "black", \
     tan(x) lc "sea-green", \
     -1/tan(x) lc "blue" title "cot(x)", \
     sqrt((z0/x)**2 - 1) lc "red", \
     '+' using (z0):(0) with points pt 7 lc "red" title "(z0,0)", \
     '+' using (pi/2):(0) with points pt 7 lc "blue" title "(pi/2,0)", \
     '+' using (pi):(0) with points pt 7 lc "sea-green" title "(pi,0)", \
     '+' using (3*pi/2):(0) with points pt 7 lc "blue" title "(3pi/2,0)", \
     '+' using (2*pi):(0) with points pt 7 lc "sea-green" title "(2pi,0)"
