import random
lst = [random.randint(0,10) for _ in range(20)]

def freq_counter(lst):
  freq_dict = {}
  for e in lst:
    freq_dict[e] = freq_dict.get(e, 0) + 1
  return freq_dict

def histogram(lst):
  freq_dict = freq_counter(lst)
  for tup in freq_dict.items():
    print(tup[0], "*" * tup[1])

print(lst)
print(freq_counter(lst))
histogram(lst)