# 1,1 1,2 1,3
# 2,1 2,2 2,3
# 3,1 3,2 3,3

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

#             0,-2
#       -1,-1 0,-1 1,-1
#  -2,0 -1,0  0,0  1,0 2,0
#       -1,1  0,1  1,1
#             0,2

layout = {
    -2: (0, 0),
    -1: (-1, 1),
    0: (-2, 2),
    1: (-1, 1),
    2: (0, 0),
}


def get_key(loc):
    return {
        -2: [1],
        -1: [2, 3, 4],
        0: [5, 6, 7, 8, 9],
        1: ['A', 'B', 'C'],
        2: ['D'],
    }[loc[1]][loc[0] + 2 - abs(loc[1])]


def move(key, dir):
    y_min, y_max = layout[key[0]]
    x_min, x_max = layout[key[1]]

    if dir == 'U':
        key[1] -= 1 if key[1] > y_min else 0
    elif dir == 'D':
        key[1] += 1 if key[1] < y_max else 0
    elif dir == 'L':
        key[0] -= 1 if key[0] > x_min else 0
    elif dir == 'R':
        key[0] += 1 if key[0] < x_max else 0


key = [-2, 0]
for line in open('input.txt'):
    for dir in line.strip():
        move(key, dir)
    print(get_key(key), end='')
print()
