def show_progress(repeat, character='*'):
    for r in range(repeat):
        print(character, end='')
    print()
    print(character*repeat)

show_progress(10)

