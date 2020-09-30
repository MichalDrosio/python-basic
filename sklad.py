


w_s = input('Podaj ilosc wagonw w przedzoale (1 ≤ 𝑊 ≤ 2*10*6) i liczbe ton cementu w pzrdziale (1 ≤ 𝑆 ≤ 2*10**9):\n')

ws = w_s.split( )

w = int(ws[0])
s = int(ws[1])





ilosc_ton = input(f'Podaj {w} ilosci cementu, oddzielonych spacja')
tony = ilosc_ton.split(' ')
array = [int(t) for t in tony]






def f():
    count = []
    while array:
        a = []
        for i in array:
            a.append(i)
            if sum(a) == s:
                count.append(a)
                break
        array.pop(0)
    return count


def print_results():
    min = None
    for i in f():
        if min == None:
            min = len(i)
        elif min != 0:
            if len(i) < min:
                min = len(i)
    return min


print(print_results())
