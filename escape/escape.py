from re import sub

total = 0
for line in open('input.txt'):
    line = line.strip()
    l_count = len(line)
    # line = sub(r'\\\\|\\x[0-9a-fA-F]{2}|\\"', '*', line)[1:-1]
    line = line.replace('\\', '\\\\')
    line = line.replace('\"', '\\"')
    line = f'"{line}"'
    # line = line.replace('\"', '\\"')
    new_count = len(line)
    total += new_count - l_count
print(total)
