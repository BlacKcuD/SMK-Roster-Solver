import collections
from constraint import *

Raider = collections.namedtuple('Raider', 'name role range c')
raiders = [
    Raider(name='Casiopia', role='tank', range='melee', c='paladin'),
    Raider(name='Blunaglaive', role='dps', range='melee', c='demonhunter'),
    Raider(name='Stdbrocoli', role='heal', range='range', c='druid'),
    Raider(name='StdFerukos', role='dps', range='range', c='druid'),
    Raider(name='Fearoshimato', role='dps', range='range', c='warlock'),
    Raider(name='Alphamonk', role='tank', range='melee', c='monk')
]

slots = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5']

def onlyOneTank(slot1, slot2, slot3, slot4, slot5):
    slots = [slot1, slot2, slot3, slot4, slot5]
    tanks = 0
    for s in slots:
        if s.role == 'tank':
            tanks += 1
    return tanks == 1

problem = Problem()
for s in slots:
    problem.addVariable(s, raiders)
problem.addConstraint(FunctionConstraint(onlyOneTank), slots)
problem.addConstraint(AllDifferentConstraint())
solutions = problem.getSolutions()
print(solutions[0])
print(solutions[1])
