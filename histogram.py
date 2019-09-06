lst = [1, 1, 2, 3, 3, 3, 3, 5]

def freq_counter(lst):
  freq_dict = {}
  for e in lst:
    freq_dict[e] = freq_dict.get(e, 0) + 1
  return freq_dict

print(freq_counter(lst))
