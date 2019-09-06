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

range_size = max_value - min_value
bin_size   = range_size / 10
print('range size: %.2f' %range_size)
print('bin size: %.2f' %bin_size)
print('first bin is [%.2f, %.2f)' %(min_value, min_value + bin_size))

numbers_in_first_bin = hist[0]

print('first 10 datapoints after sorting: ')
for _ in sorted(d)[:numbers_in_first_bin + 1]: print('%.2f' %_)