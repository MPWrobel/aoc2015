import itertools
import math

presents = [int(present) for present in open('presents.txt')]
total = sum(presents)
group = total // 4


if __name__ == '__main__':
    combinations = itertools.combinations(presents, 4)
    compositions = [combination
                    for combination in combinations
                    if sum(combination) == group]
    min_qe = math.inf
    for composition in compositions:
        qe = math.prod(composition)
        if qe < min_qe:
            min_qe = qe

    print(min_qe)
