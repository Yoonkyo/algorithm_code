import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

N = 20             # Number of points
xlim = -1350, 1350    # X-axis range for plot
ylim = -1350, 1350    # Y-axis range for plot

# Drawing Circle
theta = np.linspace(0, 2*np.pi, 100)

r = 900

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

# Nonce in circle
x_in = []
y_in = []
random_list = np.linspace(0, r, 10)
for i in range(10):
    ran_angle = np.random.randint(360)
    ran_r = random_list[i]
    x_in.append(ran_r * np.cos(ran_angle))
    y_in.append(ran_r * np.sin(ran_angle))

"""
for i in range(10):
    ran_angle = np.random.randint(360)
    if i == 0:
        ran_r = 0
    elif i == 9:
        ran_r = r
    else:
        ran_r = np.random.randint(r)
    x_in.append(ran_r * np.cos(ran_angle))
    y_in.append(ran_r * np.sin(ran_angle))
"""

# Nonce over circle
x_out = []
y_out = []
for i in range(10):
    ran_angle = np.random.randint(360)
    ran_r = np.random.randint(r, 1500)
    x_out.append(ran_r * np.cos(ran_angle))
    y_out.append(ran_r * np.sin(ran_angle))

# Save data as csv file
f = open('cep_test.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([" ", "X", "Y", "Status"])
for i in range(10):
    wr.writerow([i+1, x_in[i], y_in[i], "HIT"])
for i in range(10):
    wr.writerow([i+11, x_out[i], y_out[i], "MISS"])
f.close()

# Plotting
fig, ax = plt.subplots(1)

ax.plot(x1, x2)
ax.set_aspect(1)
# plt.plot(x, y, marker='o', linestyle='-', label='Samples')
plt.scatter(x_in, y_in, color='r', label="Hit")
plt.scatter(x_out, y_out, color='b', label="Miss")

plt.xlim(xlim)
plt.ylim(ylim)

plt.grid(linestyle='--')

plt.xlabel("X(m)")
plt.ylabel("Y(m)")
plt.title('CEP Sample (radius: 900m)', fontsize=12)
# plt.legend(loc='best')
plt.legend(loc='lower right')

# plt.savefig("cep_sample.jpg")
plt.show()
