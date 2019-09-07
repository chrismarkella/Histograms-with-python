import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from scipy import stats

np.random.seed(444)

d = np.random.laplace(loc = 20, scale = 3, size = 1000)

sns.set_style('darkgrid')
sns.distplot(d, fit = stats.laplace, kde = False)

plt.show()
