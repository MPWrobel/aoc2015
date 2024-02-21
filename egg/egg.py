from itertools import combinations

containers = list(int(cont) for cont in open('input.txt'))
number = 0
for i in range(1, len(containers) + 1):
    comb = list(comb for comb in combinations(
        containers, i) if sum(comb) == 150)
    number += len(comb)
    if number > 0:
        print(number)
print(number)
