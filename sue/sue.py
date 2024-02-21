auntie = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

aunts: dict = {}


def load():
    for line in open('input.txt'):
        name, infos = line.split(': ', 1)
        aunts[name] = {}
        for info in infos.split(', '):
            key, val = info.split(': ')
            aunts[name][key] = int(val)


load()
for name, info in aunts.items():
    for key, val in info.items():
        if key == 'cats' or key == 'trees':
            if auntie[key] >= val:
                break
        elif key == 'pomeranians' or key == 'goldfish':
            if auntie[key] <= val:
                break
        else:
            if auntie[key] != val:
                break
    else:
        print(name)
