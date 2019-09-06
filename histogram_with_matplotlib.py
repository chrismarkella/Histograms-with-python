import numpy as np
import matplotlib.pyplot as plt

np.random.seed(444)
np.set_printoptions(precision = 2)

d = np.random.laplace(loc = 20, scale = 3, size = 1000)

n, bins, patches = plt.hist(x = d, bins = 'auto', color = '#0504aa', alpha = 0.7, rwidth = 0.85)
plt.grid(axis = 'y', alpha = 0.75)
plt.xlabel = ('Value')
plt.ylabel('Frequency')
plt.title("Chris's first histogram")
plt.text(23, 24, r'$\mu = 15, b = 3$')
maxfreq = n.max()
plt.ylim(top = np.ceil(maxfreq / 10) * 10 if maxfreq % 10 else  maxfreq + 10)

plt.show()