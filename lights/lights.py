lights: list = []
for line in open('input.txt'):
    lights.append([])
    for c in line.strip():
        lights[-1].append(True if c == '#' else False)
lights[0][0] = True
lights[0][99] = True
lights[99][0] = True
lights[99][99] = True


def count():
    on = 0
    for row in lights:
        for light in row:
            if light:
                on += 1
    return on


def check(copy, x, y):
    on = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            xx, yy, = x + j, y + i
            if i == 0 and j == 0:
                continue
            if 0 > yy or yy >= len(copy):
                continue
            if 0 > xx or xx >= len(copy[yy]):
                continue
            if copy[yy][xx]:
                on += 1
    return on


def step():
    copy = [[light for light in row] for row in lights]
    for y, row in enumerate(copy):
        for x, light in enumerate(row):
            if y in (0, 99) and x in (0, 99):
                continue
            on = check(copy, x, y)
            if light:
                if on not in (2, 3):
                    lights[y][x] = False
            else:
                if on == 3:
                    lights[y][x] = True


for _ in range(100):
    # for row in lights:
    #     print(*['#' if x else '.' for x in row], sep='')
    # print(count(), '\n')
    step()
print(count())
