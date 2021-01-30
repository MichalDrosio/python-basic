def tower_builder(n_floors):
    tower = []
    floor = ''
    print(range(n_floors))
    for f in range(n_floors):
        print(f'index:{f}')
        stars = '*' * (f * 2 + 1)
        print(f'stars:{stars}')
        spaces = ' ' * (n_floors - f - 1)
        print(f'spaces:{len(spaces)}')
        floor = spaces + stars + spaces
        print(f'floor:{floor}')
        print('-------------------------------------------')
        tower.append(floor)

    return tower


print(tower_builder(4))
