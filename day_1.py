import math


def calc_fuel(mass):
    return math.floor(mass / 3) - 2


def calc_fuel_complete(mass):
    """Calculates fuel requirements for a given
    mass, taking into account that additional
    fuel counts as extra mass, needing more fuel."""
    total = 0
    while (fuel := calc_fuel(mass)) >= 0:
        total += fuel
        mass = fuel

    return total


def part_one(file):
    with open(file) as f:
        values = f.readlines()
    values = [int(x.strip()) for x in values]

    total = 0
    for value in values:
        total += calc_fuel(value)
    print(total)


def part_two(file):
    with open(file) as f:
        values = f.readlines()
    values = [int(x.strip()) for x in values]

    total = 0
    for value in values:
        total += calc_fuel_complete(value)
    print(total)


if __name__ == '__main__':
    part_two('inputs/day_1.txt')
