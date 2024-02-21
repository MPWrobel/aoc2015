visited = []

def was_visited(loc):
    if loc in visited:
        print(loc)
        print(abs(loc[0]) + abs(loc[1]))
        return True
    return False

def main():
    dir = (0, 1)
    loc = (0, 0)

    for move in open('dirs.txt').read().split(', '):
        dist = int(move[1:])
        if move[0] == 'R':
            if dir == (0, 1):
                dir = (1, 0)
            elif dir == (1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (-1, 0)
            elif dir == (-1, 0):
                dir = (0, 1)
        elif move[0] == 'L':
            if dir == (0, 1):
                dir = (-1, 0)
            elif dir == (-1, 0):
                dir = (0, -1)
            elif dir == (0, -1):
                dir = (1, 0)
            elif dir == (1, 0):
                dir = (0, 1)

        prev = loc
        loc = loc[0] + dir[0] * dist, loc[1] + dir[1] * dist

        if dir[0]:
            print('h', prev, '->', loc)
            for x in range(abs(loc[0] - prev[0])):
                step = (prev[0] + x * dir[0], prev[1])
                if was_visited(step):
                    return
                print('\t', step)
                visited.append(step)
        else:
            print('v', prev, '->', loc)
            for y in range(abs(loc[1] - prev[1])):
                step = (prev[0], prev[1] + y * dir[1])
                if was_visited(step):
                    return
                print('\t', step)
                visited.append(step)


if __name__ == '__main__':
    main()
