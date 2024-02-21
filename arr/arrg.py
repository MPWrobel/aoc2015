from itertools import permutations

family: dict = {}


def mem_to_i(mem, dic):
    return


for line in open('input.txt'):
    member, _, op, pts, *_, neighbour = line.split()  # type: ignore
    pts = int(pts)  # type: ignore
    neighbour = neighbour[:-1]
    try:
        family[member]
    except KeyError:
        family[member] = {}
    finally:
        member = family[member]
        member[neighbour] = pts if op == 'gain' else -pts  # type: ignore

for member in family.values():
    member['me'] = 0  # type: ignore
family['me'] = {member: 0 for member in family.keys()}
print(family)

last = len(family) - 1
best = 0
for arr in permutations(range(len(family))):
    sum = 0
    for i, mem in enumerate(arr):
        left = i - 1 if i > 0 else last
        right = i + 1 if i < last else 0
        left, right = arr[left], arr[right]
        items = tuple(family.keys())
        left, right = items[left], items[right]  # type: ignore
        member = tuple(family.values())[mem]
        sum += member[left] + member[right]  # type: ignore
    if sum > best:
        best = sum

print(best)
