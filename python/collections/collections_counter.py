from collections import Counter

profit = 0
shoes = int(input())
temp = list(map(int, input().split(' ')))
sizes = Counter(temp)

for _ in range(int(input())):
    customer = list(map(int, input().split(' ')))
    size = sizes.get(customer[0])
    if size != None:
        if sizes[customer[0]] > 0:
            profit += customer[1]
            sizes[customer[0]] -= 1

print(profit)
