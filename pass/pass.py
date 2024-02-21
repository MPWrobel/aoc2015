INPUT = 'vzbxkghb'


def inc(string):
    chars = [ord(c) for c in string]
    i = len(chars) - 1
    while True:
        if chars[i] < ord('z'):
            chars[i] += 1
            break
        else:
            chars[i] = ord('a')
            i -= 1
    return ''.join([chr(c) for c in chars])


def check(passw):
    prev = '#'
    pairs = 0
    increase = False
    rep = 0
    inc = 0
    for c in passw:
        if c in ('i', 'o', 'l'):
            return False
        else:
            if prev == c:
                rep += 1
                if rep == 1:
                    pairs += 1
                elif rep == 2:
                    pairs -= 1
            else:
                rep = 0

            if inc == 2:
                increase = True

            if ord(prev) + 1 == ord(c):
                inc += 1
            else:
                inc = 0

            prev = c
    return pairs >= 2 and increase


password = inc('vzbxxyzz')
while not check(password):
    password = inc(password)

print(password)
