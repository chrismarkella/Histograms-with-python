import numpy as np

np.random.seed(444)
np.set_printoptions(precision = 2)

# This generates 1000 datapoints in an array
d = np.random.laplace(loc = 20, scale = 3, size = 1000)

print
print('first five datapoints:', end = ' ')
for num in d[:5]:
  print('%.2f' %num, end = ", ")
print('\n', end = '\n')

hist, bin_edges = np.histogram(d)

# hist shows how many numbers fall into each bins
print(hist)
print(bin_edges)

min_value, max_value = min(d), max(d)
print('min: %.2f, max: %.2f' %(min_value, max_value))