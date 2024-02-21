from re import compile

registers = {'a': 1, 'b': 0}
program = []

regex = compile(r'(\w{3}) (a|b)?(?:, )?(?:(\+|-)(\d+))?')
for line in open('program.txt'):
    program.append(regex.findall(line)[0])

i = 0
while i < len(program):
    ins, reg, dir, num = program[i]
    jump = False
    match ins:
        case 'inc':
            registers[reg] += 1
        case 'tpl':
            registers[reg] *= 3
        case 'hlf':
            registers[reg] //= 2
        case 'jmp':
            jump = True
        case 'jie':
            if registers[reg] % 2 == 0:
                jump = True
        case 'jio':
            if registers[reg] == 1:
                jump = True
    if jump:
        num = int(num)
        i += num if dir == '+' else -num
    else:
        i += 1

print(registers)
