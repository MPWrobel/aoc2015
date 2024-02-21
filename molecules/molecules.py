from pprint import pprint
from sys import exit

reps = []
sp = []
rsp = ''


def isolate(mol):
    elements = []
    for i, c in enumerate(mol):
        if c == 'e':
            elements.append(c)
        elif i + 1 < len(mol) and mol[i + 1].islower() and mol[i + 1] != 'e':
            elements.append(mol[i:i + 2])
        elif c.isupper():
            elements.append(c)
    return elements


with open('input.txt') as f:
    for line in f:
        if line == '\n':
            break
        src, dest = line.strip().split(' => ')
        reps.append((src, dest))
    prev = ''
    rsp = f.readline().strip()
    sp = isolate(rsp)

combs = set()
for src, dest in reps:
    for i, x in enumerate(sp):
        if x == src:
            np = list(sp)
            np[i] = dest
            combs.add(''.join(np))
print(len(combs))


# def branch(mol, r=0):
#     print(len(mol))
#     if r == 8:
#         return
#     for i, el in enumerate(mol):
#         for _, dest in [src for src in reps if src[0] == el]:
#             nmol = list(mol)
#             nmol[i] = dest
#             nnmol = []
#             for x in nmol:
#                 if type(x) is str:
#                     nnmol.append(x)
#                 else:
#                     for y in x:
#                         nnmol.append(y)
#             branch(nnmol, r + 1)


reps = [(dest, src) for src, dest in reps]
cache: dict = {}


def solve():
    n = 0
    med = rsp
    while med != 'e':
        for src, dest in reps:
            if src in med:
                med = med.replace(src, dest, 1)
                n += 1
    print(n)


def branch(mol, r=1):
    pprint(len(mol))
    branches = []
    for dest, src in reps:
        if (i := mol.find(src)) != -1:
            left, right = mol[:i], mol[i:]
            nmol = left + right.replace(src, dest, 1)
            branches.append(nmol)
    cache[mol] = branches
    for nmol in branches:
        if nmol not in cache:
            branch(nmol, r + 1)
    return branches


solve()
print('finished')
