# Given an array of strings, sort the array into order of weight from light to heavy.
#
# Weight units are grams(G), kilo-grams(KG) and tonnes(T).
#
# Arrays will always contain correct and positive values aswell as uppercase letters.


def arrange(arr):
    result = []
    for i in arr:
        if 'T' in i:
            result.append((int(i[:-1])*1000, i))
        elif 'K' in i:
            result.append((int(i[:-2]), i))
        else:
            result.append((int(i[:-1])/1000, i))

    return [i[1] for i in sorted(result)]

print(arrange(["200G", "300G", "150G", "100KG"]))