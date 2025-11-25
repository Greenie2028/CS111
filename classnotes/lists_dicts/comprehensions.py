class dict:
    def __str__(self):
        for k, v in self:
            print(f"{k}: {v}")
from random import randint
lst = [2*i for i in range(randint(1,10))]
print("[",end="")
for i in range(len(lst)):
    if i == len(lst) - 1:
        print(f"{lst[i]}]")
    else:
        print(lst[i])
dictionary = {i: i**2 for i in range(1,10)}
c = 0
for k, v in dictionary.items():
    if c == 0:
        print("{" + f"{k}: {v}", end="")
        c += 1
    else:
        print(f"\n{k}: {v}", end = "")
print("}")