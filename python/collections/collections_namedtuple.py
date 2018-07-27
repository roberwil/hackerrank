from collections import namedtuple
mean = 0.0
n = int(input())
Student = namedtuple('Student', input())
for _ in range(n):
    txt = input().split()
    guy = Student(txt[0], txt[1], txt[2], txt[3])
    mean += float(guy.MARKS)

print(round(mean/n, 2))
