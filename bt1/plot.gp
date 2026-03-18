reset
set angles radians
set terminal pngcairo size 800,400

set output "images/gnuplot-83-2.png"

set samples 1000
set xrange [-4:4]
set yrange [-100:10]

N = 3

plot "data/potential.txt" w l lc "black" notitle, \
     for [i=1:N] sprintf("data/energy-%d.txt", i) w l lc "red" dt 2 notitle, \
     for [i=1:N] sprintf("data/wave-%d.txt", i) w l lc "blue" notitle
