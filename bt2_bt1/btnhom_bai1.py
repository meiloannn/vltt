import numpy as np
import matplotlib.pyplot as plt
import random

N_steps = 1000   # Số bước trong một lần đi
K_trials = 100   # Số lần thử độc lập

def random_2D():
    dx_prime = random.uniform(-1, 1)
    dy_prime = random.uniform(-1, 1)
    L = np.sqrt(dx_prime**2 + dy_prime**2)
    dx = dx_prime / L
    dy = dy_prime / L
    return dx, dy

R2_trials = []  # R^2 

for trial in range(K_trials):
    x, y = 0.0, 0.0
    for step in range(N_steps):
        dx, dy = random_2D()
        x += dx
        y += dy
    R2 = x**2 + y**2
    R2_trials.append(R2)

R2_mean = np.mean(R2_trials) # trung bình của (R^2)_K
R_rms = np.sqrt(R2_mean)

print(f"R^2 trung bình qua {K_trials} lần thử: {R2_mean:.4f}")
print(f"R_rms = {R_rms:.4f}")

# ----------------------------
# Hình 4.4.a
# ----------------------------
num_walks = 7

plt.figure(figsize=(4,4))
data = []  # Lưu tất cả walk

for _ in range(num_walks):
    x, y = 0.0, 0.0
    X, Y = [x], [y]
    for _ in range(N_steps):
        dx, dy = random_2D()
        x += dx
        y += dy
        X.append(x)
        Y.append(y)
    plt.plot(X, Y)
    data.append(list(zip(X,Y)))  # Lưu walk vào data

plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"{num_walks} Random Walks")
plt.grid(True)
plt.axis('equal')
plt.show()

# Xuất ra file
with open("table4.4a.txt", "w") as f:
    # Dòng header
    f.write(f"{'step':<5}")
    for w in range(num_walks):
        f.write(f"{'Walk'+str(w+1):^16}")
    f.write("\n")

    # Dòng x y
    f.write(f"{'':<5}")
    for w in range(num_walks):
        f.write(f"{'x'+str(w+1):>8}{'y'+str(w+1):>8}")
    f.write("\n")

    # Data
    for i in range(N_steps+1):
        f.write(f"{i:<5}")
        for w in range(num_walks):
            x, y = data[w][i]
            f.write(f"{x:>8.3f}{y:>8.3f}")
        f.write("\n")
###GNUPLOT
## Hình 4.4.a: Random Walks
# set title "7 Random Walks"
# set xlabel "X"
# set ylabel "Y"
# set grid
# set key left top
# set size square

# # Vẽ các walk
# plot for [i=2:15:2] "table4.4.a.txt" using i:i+1 with lines lw 1.5 title columnheader(i)

# ----------------------------
# Vẽ đồ thị 4.4.b
# ----------------------------
N_values = np.arange(1, N_steps+1, 10)  # Chọn bước theo khoảng cách
R_rms_values = []

for N in N_values:
    R2_temp = []
    for trial in range(K_trials):
        x, y = 0.0, 0.0
        for step in range(N):
            dx, dy = random_2D()
            x += dx
            y += dy
        R2_temp.append(x**2 + y**2)
    R_rms_values.append(np.sqrt(np.mean(R2_temp)))

plt.figure(figsize=(3,3))
plt.plot(np.sqrt(N_values), R_rms_values, 'b-', label="R_rms từ mô phỏng")
plt.plot(np.sqrt(N_values), np.sqrt(N_values), 'r--', label="R_rms ~ √N (lý thuyết)")
plt.xlabel("√N")
plt.ylabel("R_rms")
plt.title("R_rms theo √N")
plt.legend()
plt.grid(True)
plt.show()
import numpy as np
# ----------------------------
# lưu file 4.4.b
# ----------------------------

with open("table4.4b.txt", "w") as f:
    f.write(f"{'sqrt(N)':>10}{'R_rms':>10}\n")
    
    # Dữ liệu
    for N, Rrms in zip(N_values, R_rms_values):
        f.write(f"{np.sqrt(N):>10.3f}{Rrms:>10.3f}\n")
        ##GNUPLOT
# # Hình 4.4.b: R_rms theo √N
# set title "R_rms theo √N"
# set xlabel "√N"
# set ylabel "R_rms"
# set grid
# set key left top

# plot "table4.4b.txt" using 1:2 with linespoints lt rgb "blue" lw 2 pt 7 title "R_rms từ mô phỏng", \
#      x with lines lt rgb "red" lw 2 title "R_rms ~ √N (lý thuyết)"