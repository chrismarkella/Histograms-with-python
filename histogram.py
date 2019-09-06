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

print(lst)
print(freq_counter(lst))
histogram(lst, True)