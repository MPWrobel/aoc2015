possible = 0
triangles = ([], [], [])

for line in open('input.txt'):
    dimensions = line.split()

    for i, triangle in enumerate(triangles):
        triangles[i].append(int(dimensions[i]))

    if len(triangles[0]) < 3:
        continue

    for triangle in triangles:
        a, b, c = triangle
        if a + b > c and a + c > b and b + c > a:
            possible += 1

        triangle.clear()

print(possible)
