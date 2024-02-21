from copy import deepcopy
from math import inf


spells = [
    {
        'name': 'missle',
        'mana': 53,
        'instant': True,
        'hp': 0,
        'damage': 4,
    },
    {
        'name': 'drain',
        'mana': 73,
        'instant': True,
        'hp': 2,
        'damage': 2,
    },
    {
        'name': 'shield',
        'mana': 113,
        'turns': 6,
        'instant': False,
    },
    {
        'name': 'poison',
        'mana': 173,
        'turns': 6,
        'instant': False,
    },
    {
        'name': 'recharge',
        'mana': 229,
        'turns': 5,
        'instant': False,
    },
]


mana_min = inf
win = None


class State:
    def __init__(self, mana=250, hp=10, hp_op=13, boss_dmg=8):
        self.boss_dmg = boss_dmg
        self.logs = ""
        self.effects = {}
        self.armor = 0
        self.mana = mana
        self.hp = hp
        self.hp_op = hp_op
        self.cost = 0

    def cast(self, spell):
        self.log(f"Player casts {spell['name'].title()} ")
        self.mana -= spell['mana']
        self.cost += spell['mana']

        if spell['instant']:
            heal, damage = spell['hp'], spell['damage']

            self.log(f"dealing {damage} damage")
            self.log(f" and healing {heal} hit points\n" if heal else "\n")

            self.hp += heal
            self.hp_op -= damage
        else:
            self.log("\n")

            self.effects[spell['name']] = spell['turns'] - 1

    def attack(self):
        damage = self.boss_dmg - self.armor
        self.log(f"Boss attacks for {damage} damage\n")

        self.hp -= damage if damage > 1 else 1

    def stats(self, entity):
        self.log(f"\n-- {entity} turn --\n",
                 f"- Player has {self.hp} hit points, ",
                 f"{self.armor} armor, {self.mana} mana\n",
                 f"- Boss has {self.hp_op} hit points\n")

    def log(self, *msgs):
        for msg in msgs:
            self.logs += msg

    def check(self):
        if self.mana == 0 or self.hp <= 0:
            self.log("\nGAME OVER")
            return False
        elif self.hp_op <= 0:
            self.log("\nThis kills, the boss, and the player wins.")
            global mana_min, win
            if mana_min > self.cost:
                mana_min = self.cost
                win = self.logs
            return True

    def effect(self):
        logs = ""
        worn_off = []
        for key in self.effects:
            if (timer := self.effects[key]) == 0:
                worn_off.append(key)
            else:
                self.effects[key] -= 1

            if key == 'shield':
                logs = f"Shield's timer is now {timer}\n"

                self.armor = 7
                continue

            if key == 'poison':
                logs += "Poison deals 3 damage"

                self.hp_op -= 3
            elif key == 'recharge':
                logs += "Recharge provides 101 mana"

                self.mana += 101
                # self.cost -= 101

            logs += f"; its timer is now {timer}.\n"

        for key in worn_off:
            del self.effects[key]

        return logs


def turn(game):
    for spell in spells:
        g = deepcopy(game)

        timer = g.effects.get(spell['name'])
        available = timer is None or timer == 0
        if g.mana < spell['mana'] or not available:
            continue

        g.armor = 0
        g.hp -= 1
        if g.check() is not None:
            return
        logs = g.effect()
        g.stats("Player")
        g.log(logs)
        if g.check() is not None:
            return
        g.cast(spell)
        if g.check() is not None:
            return

        g.armor = 0
        logs = g.effect()
        g.stats("Boss")
        g.log(logs)
        if g.check() is not None:
            return
        g.attack()
        if g.check() is not None:
            return

        if g.cost > mana_min:
            return

        turn(g)


if __name__ == '__main__':
    turn(State(
        hp=50,
        mana=500,
        hp_op=55,
        boss_dmg=8
    ))
    print(mana_min)
    print(win)
