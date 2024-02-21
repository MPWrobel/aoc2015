from json import loads


def json_sum(value):
    sum = 0
    if type(value) is int:
        return value
    elif type(value) is list:
        for el in value:
            sum += json_sum(el)
        return sum
    elif type(value) is dict:
        for key, val in value.items():
            if val == 'red':
                return 0
            else:
                sum += json_sum(val)
        return sum
    return 0


json = loads(open('input.txt').read())
print(json_sum(json))
