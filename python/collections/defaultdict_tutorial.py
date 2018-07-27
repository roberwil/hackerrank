from collections import defaultdict

group_a = defaultdict(list)
group_b = []
a, b = list(map(int, input().split()))

for x in range(1, a + 1):
    group_a[input()].append(x)

for x in range(b):
    item_b = input()
    item_a = group_a[item_b]
    if len(item_a) > 0:
        txt = str(item_a)
        print(" ".join(txt[1:len(txt) - 1].split(', ')))
    else:
        print ('-1')
