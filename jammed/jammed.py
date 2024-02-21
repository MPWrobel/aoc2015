# type: ignore
letters = [{} for _ in range(len(open('input.txt').readline().strip()))]

for line in open('input.txt'):
    for i, c in enumerate(line.strip()):
        if c not in letters[i]:
            letters[i][c] = 1
        else:
            letters[i][c] += 1

for letter in letters:
    correct = ('', 1000)
    for option in letter.items():
        if option[1] < correct[1]:
            correct = option
    print(correct[0], end='')
print()
