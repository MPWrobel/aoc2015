# type: ignore

from re import findall


def is_aba(string):
    return string[0] == string[2] and string[0] != string[1]


def is_abba(string):
    return string[0] == string[3] and string[1] == string[2] and string[0] != string[1]


def has_abba(string):
    four_letters = findall(r'(?=([a-z]{4}))', string)

    for four_letter in four_letters:
        if is_abba(four_letter):
            return True

    return False


def get_abas(string):
    three_letters = findall(r'(?=([a-z]{3}))', string)

    abas = []
    for three_letter in three_letters:
        if is_aba(three_letter):
            abas.append(three_letter)

    return abas


tls_support = 0
for line in open('input.txt'):
    supernet = ['']
    hypernet = []
    add_to = supernet

    for c in line.strip():
        if c == '[':
            add_to = hypernet
            add_to.append('')
        elif c == ']':
            add_to = supernet
            add_to.append('')
        else:
            add_to[-1] += c

    supernet_abas = []
    for abas in (get_abas(net) for net in supernet):
        supernet_abas += abas

    hypernet_abas = []
    for abas in (get_abas(net) for net in hypernet):
        hypernet_abas += abas

    for aba in supernet_abas:
        complementary = aba[1] + aba[0] + aba[1]
        if complementary in hypernet_abas:
            tls_support += 1
            break

print(tls_support)
