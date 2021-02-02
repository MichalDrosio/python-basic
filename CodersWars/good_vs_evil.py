def good_vs_evil(good, evil):
    goods = good.split()
    evils = []
    for i in goods:
        try:
            good = int(i)
            evils.append(good)
        except ValueError:
            print()
    return evils







good = 'Hobbits: 1 Men: 2 Elves: 3 Dwarves: 3 Eagles: 4 Wizards: 10'
evil = 'Orcs: 1 Men: 2 Wargs: 2 Goblins: 2 Uruk Hai: 3 Trolls: 5 Wizards: 10'

print(good_vs_evil(good, evil))