from random import randint
heads = 0
tails = 0
for trial in range(0, 1000):
    while randint(0,1) == 0:
        tails = tails + 1
    heads = heads + 1
print("heads/ tails", heads/tails)
print(heads)
print(tails)
