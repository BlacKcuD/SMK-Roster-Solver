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

def debugContraint(*args):
    numTanks = 0
    numHeals = 0
    numPriests = 0
    numMages = 0
    numWarriors = 0
    numMonks = 0
    numDemonHunters = 0
    for s in args:
        if s.role == 'tank':
            numTanks += 1
        if s.role == 'heal':
            numHeals += 1
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
    print('Tanks: %d, Heals: %d, assignment: %s' % (numTanks, numHeals, args))
    return True

# alphabet salat arp version
def reduceConstraint(*args):
    for i, el in enumerate(args[1:]):
        if key(el) < key(args[i]):
            return False
    return True

# alphabet salat frosch version
def ascendingOrder(*args):
    last_slot_name = next(iter(args)).name

    for slot in args:
        if slot.name < last_slot_name:
            return False
        last_slot_name = slot.name
    return True

# Problem Calculation
problem = Problem()
tanks = [r for r in raiders if r.role == 'tank']
dps = [r for r in raiders if r.role == 'dps']
healers = [r for r in raiders if r.role == 'heal']

numTanks = 2
numHeals = 5
numDps = len(slots) - numTanks - numHeals

tankSlots = ['slot%d' % i for i in range(1, numTanks+1)]
dpsSlots = ['slot%d' % i for i in range(numTanks+1, numDps+numTanks+1)]
healSlots = ['slot%d' % i for i in range(numDps+numTanks+1, len(slots)+1)]

problem.addVariables(['slot1', 'slot2'], tanks)
problem.addVariables(['slot%d' % i for i in range(3, 16)], dps)
problem.addVariables(['slot16', 'slot17', 'slot18', 'slot19', 'slot20'], healers)

problem.addConstraint(debugContraint, slots)
problem.addConstraint(AllDifferentConstraint())
problem.addConstraint(ascendingOrder, tankSlots)
problem.addConstraint(ascendingOrder, dpsSlots)
problem.addConstraint(ascendingOrder, healSlots)
solutions_iter = problem.getSolutionIter()
first_solution = list(solutions_iter)[0]
print(first_solution)
