from collections import deque
numbers = deque()
for _ in range(int(input())):
    temp = input().split()
    op = temp[0]
    n = temp[1] if len(temp) > 1 else None
    if op == 'append':
        numbers.append(n)
    elif op == 'appendleft':
        numbers.appendleft(n)
    elif op == 'pop':
        numbers.pop()
    else:
        numbers.popleft()
print(" ".join(map(str, numbers)))
