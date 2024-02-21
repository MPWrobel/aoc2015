ingredients: list = []
for line in open('input.txt'):
    props = {}
    ingredient, properties = line.split(': ')
    for property in properties.split(', '):
        key, val = property.split()
        props[key] = int(val)
    props['calories']
    ingredients.append(props)


def combine(sum, start=0):
    return [(i, sum - i) for i in range(start, int(sum / 2) + 1)]


def recombine(comb):
    out = []
    for c in comb:
        for cc in combine(*c[-1:]):
            out.append((*c[:-1], *cc))
    return out


def calc():
    c100 = recombine(recombine(combine(100)))
    best = 0
    for recipe in c100:
        # print(recipe)
        props = [0] * 5
        for i, amount in enumerate(recipe):
            for j, prop in enumerate(ingredients[i].values()):
                props[j] += prop * amount

        score = 1
        for p in props[:-1]:
            if p <= 0:
                break
            score *= p
        else:
            if props[4] == 500 and score > best:
                best = score

    print(best)


calc()
