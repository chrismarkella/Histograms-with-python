# Following the Tutorials from Real Python
# https://realpython.com/courses/python-histograms/

import random

lst = [random.randint(0,10) for _ in range(20)]

def freq_counter(lst: list) -> dict:
  freq_dict = {}
  for e in lst:
    freq_dict[e] = freq_dict.get(e, 0) + 1
  return freq_dict

def histogram(lst: list, reverse_order:bool = False) -> None:
  freq_dict = freq_counter(lst)

  sorted_dict_by_values = sorted(freq_dict.items(), key = lambda tup: tup[1], reverse = reverse_order)

  for tup in sorted_dict_by_values:
    print('%2d:2 %s' %(tup[0], "+" * tup[1]))

def top_freq(lst: list, rank = 1) -> tuple:
  freq_dict = freq_counter(lst)

  sorted_dict_by_values = sorted(freq_dict.items(), key = lambda tup: tup[1], reverse = True)
  return sorted_dict_by_values[rank - 1]  

print(lst)
print(freq_counter(lst))
histogram(lst, True)

print(top_freq(lst))
print(top_freq(lst, 2))
