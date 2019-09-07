import numpy as np
import pandas as pd

ages = pd.Series(
  [1, 1, 2, 2, 3, 5, 8, 10, 12, 15, 18, 18, 19, 20, 25, 30, 40, 51, 52, 70]
)
bins = [0, 10, 13, 18, 21, np.inf]
labels = ['child', 'preteen', 'teen', 'military age', 'adult']

groups = pd.cut(ages, bins = bins, labels = labels)

print(groups.value_counts())
