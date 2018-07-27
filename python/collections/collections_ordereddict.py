from collections import OrderedDict as od
items = od()
for _ in range(int(input())):
    temp = input().split()
    key = " ".join(temp[:len(temp) - 1])
    value = int(temp[len(temp) - 1])
    if key in items:
        items[key] += value
    else:
        items[key] = value
for key in items:
    print('{} {}'.format(key, items[key]))
