from itertools import combinations, product
from pprint import pprint
from re import compile

player_hp = 100
boss_hp, boss_dmg, boss_def = 0, 0, 0
for line in open('boss.txt'):
    stat, raw_val = line.split(': ')
    val = int(raw_val)
    match stat:
        case 'Hit Points':
            boss_hp = val
        case 'Damage':
            boss_dmg = val
        case 'Armor':
            boss_def = val

shop: dict = {}
key = ''

item_regex = compile(r'^(\w+)\s+(?:(\+\d+)\s+)?(\d+)\s+(\d+)\s+(\d+)$')
type_regex = compile(r'^(\w+):\s+\w+\s+\w+\s+\w+$')

for line in open('shop.txt'):
    if item := item_regex.findall(line):
        name, bonus, cost, damage, armor = item[0]
        shop[key].append({
            'name': name,
            'bonus': bonus,
            'cost': int(cost),
            'damage': int(damage),
            'armor': int(armor),
        })
    elif kind := type_regex.findall(line):
        key = kind[0]
        shop[key] = []

shop['Armor'] += [{
    'name': 'none',
    'bonus': 0,
    'cost': 0,
    'damage': 0,
    'armor': 0,
}]

shop['Rings'] += [{
    'name': 'none',
    'bonus': 0,
    'cost': 0,
    'damage': 0,
    'armor': 0,
}]

slots = ['Weapons', 'Armor']
rings = [tuple([shop['Rings'][-1]] * 2), *combinations(shop['Rings'], 2)]


def get_real_dmg(damage, op_defense):
    real_dmg = damage - op_defense
    return real_dmg if real_dmg > 1 else 1


def get_winner(player_dmg, boss_dmg):
    if player_dmg >= boss_dmg:
        return True
    else:
        return False


max_cost = 0
for eq in product(*[shop[slot] for slot in slots], rings):
    weapon, armor, (ring1, ring2) = eq

    cost = weapon['cost'] + armor['cost'] + ring1['cost'] + ring2['cost']
    player_dmg = weapon['damage'] + ring1['damage'] + ring2['damage']
    player_def = armor['armor'] + ring1['armor'] + ring2['armor']

    real_player_dmg = get_real_dmg(player_dmg, boss_def)
    real_boss_dmg = get_real_dmg(boss_dmg, player_def)

    if not get_winner(real_player_dmg, real_boss_dmg) and cost > max_cost:
        max_cost = cost
print(max_cost)
