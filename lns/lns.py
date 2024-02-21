INPUT = '1113222113'


def lns(number):
    output = ''
    prev = number[0]
    count = 1
    for digit in number[1:]:
        if digit != prev:
            output += f'{count}{prev}'
            prev = digit
            count = 1
        else:
            count += 1
    output += f'{count}{prev}'
    return output


def main():
    res = INPUT
    for _ in range(50):
        res = lns(res)
    print(len(res))


if __name__ == '__main__':
    main()
