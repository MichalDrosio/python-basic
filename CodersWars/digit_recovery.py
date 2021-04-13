DIGITS = {tuple(sorted(w)): str(i) for i, w in enumerate("ZERO ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE".split())}
print(DIGITS)

def recover(st):
    result = ""
    st_size = len(st)

    for start in range(st_size - 3 + 1):
        for size in range(3, min(5, st_size - start) + 1):
            sub_st = tuple(sorted(st[start: start + size]))
            result += DIGITS.get(sub_st, "")

    return result or "No digits found"

print(recover('NEOTWONEINEIGHTOWSVEEN'))