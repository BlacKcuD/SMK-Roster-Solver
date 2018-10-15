import collections
from constraint import *

# RAID INFO
Raider = collections.namedtuple('Raider', 'name role range c')
raiders = [
    # TANKS
    Raider(name='Casiopia', role='tank', range='melee', c='paladin'),
    Raider(name='Alphamonk', role='tank', range='melee', c='monk'),
    # DPS
    Raider(name='Danaia', role='dps', range='range', c='druid'),
    Raider(name='Stdferukos', role='dps', range='range', c='druid'),
    Raider(name='Etrix', role='dps', range='range', c='druid'),
    Raider(name='Blunaglaive', role='dps', range='melee', c='demonhunter'),
    Raider(name='Aloyra', role='dps', range='ranged', c='mage'),
    Raider(name='Mazzea', role='dps', range='ranged', c='mage'),
    Raider(name='Stdorbfuzzy', role='dps', range='ranged', c='mage'),
    Raider(name='Shekelberg', role='dps', range='ranged', c='mage'),
    Raider(name='Pandianer', role='dps', range='melee', c='monk'),
    Raider(name='Lightbringer', role='dps', range='melee', c='monk'),
    Raider(name='Spaaze', role='dps', range='melee', c='deathknight'),
    Raider(name='Catharsys', role='dps', range='range', c='priest'),
    Raider(name='Stdantea', role='dps', range='range', c='priest'),
    Raider(name='Salphina', role='dps', range='melee', c='rogue'),
    Raider(name='Allisandra', role='dps', range='melee', c='rogue'),
    Raider(name='Fearoshimato', role='dps', range='range', c='warlock'),
    Raider(name='Thalartis', role='dps', range='range', c='warlock'),
    Raider(name='Akumalolz', role='dps', range='range', c='warlock'),
    Raider(name='Artilus', role='dps', range='melee', c='warrior'),
    Raider(name='Daggoth', role='dps', range='melee', c='warrior'),
    # HEALERS
    Raider(name='Zulrakolix', role='heal', range='range', c='druid'),
    Raider(name='Elayra', role='heal', range='melee', c='monk'),
    Raider(name='Quells', role='heal', range='melee', c='paladin'),
    Raider(name='Aintnosleep', role='heal', range='range', c='priest'),
    Raider(name='Racy', role='heal', range='range', c='priest'),
    Raider(name='Stdbrocoli', role='heal', range='range', c='druid')
]

slots = ['slot1', 'slot2', 'slot3', 'slot4', 'slot5', 'slot6', 'slot7', 'slot8', 'slot9', 'slot10', 'slot11', 'slot12', 'slot13', 'slot14', 'slot15', 'slot16', 'slot17', 'slot18', 'slot19', 'slot20']
tankslots = ['slot1', 'slot2']
healslots = ['slot16', 'slot17', 'slot18', 'slot19', 'slot20']
# Constraints for group
# Exactly two tanks
def twoTanks(*args):
    numTanks = 0
    for s in args:
        if s.role == 'tank':
            numTanks += 1
    return numTanks == 2

# Exactly 4 Heals
def fourHeals(*args):
    numHeals = 0
    for s in args:
        if s.role == 'heal':
            numHeals += 1
    return numHeals == 4

# Exactly 5 Heals
def fiveHeals(*args):
    numHeals = 0
    for s in args:
        if s.role == 'heal':
            numHeals += 1
    return numHeals == 5

# Ensure all raid buffs and debuffs are present
def raidBuffs(*args):
    numPriests = 0
    numMages = 0
    numWarriors = 0
    numMonks = 0
    numDemonHunters = 0
    for s in args:
        if s.c == 'priest':
            numPriests += 1
        if s.c == 'mage':
            numMages += 1
        if s.c == 'warrior':
            numWarriors += 1
        if s.c == 'monk':
            numMonks += 1
        if s.c == 'demonhunter':
            numDemonHunters += 1
    return numPriests >= 1 and numMages >= 1 and numWarriors >= 1 and numMonks >= 1 and numDemonHunters >= 1

# Problem Calculation
problem = Problem()
for s in slots:
    problem.addVariable(s, raiders)
problem.addConstraint(FunctionConstraint(twoTanks), tankslots)
problem.addConstraint(FunctionConstraint(fiveHeals), healslots)
problem.addConstraint(FunctionConstraint(raidBuffs), slots)
problem.addConstraint(AllDifferentConstraint())
solutions = problem.getSolutions()
print(solutions[0])
