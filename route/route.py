from pprint import pprint
from itertools import permutations

connections = {}
cities = []

for line in open('input.txt'):
    conn, dista = line.strip().split(' = ')
    dist = int(dista)  # type: ignore
    city1, _, city2 = conn.split()

    if city1 not in cities:
        cities.append(city1)
    if city2 not in cities:
        cities.append(city2)

    c1, c2 = cities.index(city1), cities.index(city2)
    hash = min(c1, c2) * 100 + max(c1, c2)

    connections[hash] = dist

pprint(connections)

best = 0
b_route: tuple
for route in permutations(range(len(cities))):
    dist = 0
    for i in range(len(cities) - 1):
        c1, c2 = route[i], route[i + 1]
        hash = min(c1, c2) * 100 + max(c1, c2)
        # print(hash)
        dist += connections[hash]
    if dist > best:
        best = dist
        b_route = route

print(b_route)
print(best)
