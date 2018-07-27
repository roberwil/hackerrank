from collections import OrderedDict as od
words = od()
for _ in range(int(input())):
    txt = input()
    words[txt] = 1 if words.get(txt) == None else words[txt] + 1
print(len(words))
print(" ".join(map(str, words.values())))
