from sys import argv

signals: dict = {}
evaluated: dict = {}


def main():
    load_from_file(argv[1])
    # a = eval('a')
    # signals['b'] = str(a)
    # global evaluated
    # evaluated = {}
    print(eval('a'))


def eval(val):
    if val.isnumeric():
        return int(val)

    # if val in evaluated:
    #     return evaluated[val]

    signal = signals[val]
    if type(signal) is list:
        gate, *vals = signal
        match gate:
            case 'AND':
                res = eval(vals[0]) & eval(vals[1])
            case 'OR':
                res = eval(vals[0]) | eval(vals[1])
            case 'NOT':
                res = ~eval(vals[0])
            case 'LSHIFT':
                res = eval(vals[0]) << eval(vals[1])
            case 'RSHIFT':
                res = eval(vals[0]) >> eval(vals[1])
    else:
        res = eval(signal)
    evaluated[val] = res
    return res


def load_from_file(file_name):
    with open(file_name) as file:
        for line in file:
            signal, wire = line.strip().split(' -> ')
            signal = signal.split()
            if len(signal) == 1:
                signal = signal[0]
            elif len(signal) == 3:
                first, second, _ = signal
                signal[0], signal[1] = second, first
            signals[wire] = signal
    return signals


if __name__ == '__main__':
    main()
