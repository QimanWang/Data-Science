import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

points = [
    (-1, 3160000),
    (-0.9, 1.74506),
    (-0.8, 1.59616),
    (-0.7, 1.50936),
    (-0.6, 1.45099),
    (-0.5, 1.40955),
    (-0.4, 1.37966),
    (-0.3, 1.35844),
    (-0.2, 1.34421),
    (-0.1, 1.33601),
    (0, 1.33333),
    (0.1, 1.33601),
    (0.2, 1.34421),
    (0.3, 1.35844),
    (0.4, 1.37966),
    (0.5, 1.40955),
    (0.6, 1.45099),
    (0.7, 1.50936),
    (0.8, 1.59616),
    (0.9, 1.74506),
    (1, 3160000)
]

x = []
y = []
for point in points:
    x.append(point[0])
    y.append((point[1]))
print(x[0], y[0], x[1], y[1])

plt.figure(1)

plt.ylim(1.3,2)
plt.xlim(-1,1)
plt.plot(x,y)
plt.show()
