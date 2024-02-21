import math


def divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i in divisors:
                print(n)
            divisors.append(i)
            if i != n // i:
                if n // i in divisors:
                    print(n // i)
                divisors.append(n // i)
    return divisors


target = 29000000
# target = 60
house = 0
presents = 0
visits: dict = {}
while presents < target:
    house += 1
    elves = divisors(house)

    remove = set()
    for elf in elves:
        if visits.get(elf):
            visits[elf] += 1
        else:
            visits[elf] = 1

        if visits[elf] > 50:
            remove.add(elf)

    for elf in remove:
        elves.remove(elf)

    presents = sum(elves) * 11
    # print(house, presents, elves)

print('Result:', house)
