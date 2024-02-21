def next(prev):
    return (prev * 252533) % 33554393


def get(x, y):
    y1 = x + y - 1
    dy1 = y1 - y
    dy = dy1 + 1 + sum(range(y1))
    return dy


n = 20151125
for _ in range(get(3075, 2981) - 1):
    n = next(n)

print(n)
