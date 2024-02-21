# type: ignore
from re import compile

A = ord('a')
Z = ord('z')
CHAR_NUM = ord('z') + 1 - ord('a')


def shift_char(c, shift):
    order = ord(c) + shift
    ascii = order if order <= Z else A + (order - Z - 1)
    return chr(ascii)


def decrypt(name, id):
    id = int(id)
    shift = id % CHAR_NUM
    return ''.join((shift_char(c, shift)
                    if c != '-' else ' '
                    for c in name[:-1]))


regex = compile(r'([a-z-]+)(\d{3})\[([a-z]{5})\]')
total = 0
for room in open('input.txt'):
    name, id, checksum = regex.match(room).groups()

    letters = {}
    for c in name:
        if c == '-':
            continue

        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    letters = dict(
        sorted(letters.items(), key=lambda letter: letter[1] * 1000 + 100 - ord(letter[0]), reverse=True))

    if ''.join(list(letters.keys())[:5]) == checksum:
        total += int(id)
        print(id, decrypt(name, id))


print(total)
