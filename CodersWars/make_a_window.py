# Make me a window. I'll give you a number (N). You return a window.
#
# Rules:
#
# The window will always be 2 x 2.
#
# The window needs to have N number of periods across and N number of periods vertically in each pane.
#
# Example:
#
# N = 3
#
# ---------
# |...|...|
# |...|...|
# |...|...|
# |---+---|
# |...|...|
# |...|...|
# |...|...|
# ---------

def make_a_window(n):
    top = '-' * (2 * n + 3)
    middle = f"|{'-' * n}+{'-' * n}|"
    glasses = [f"|{'.' * n}|{'.' * n}|"] * n
    return '\n'.join([top, *glasses, middle, *glasses, top])
# print(make_a_window(3))


def make_a_window_2(num):
    window = f"{((num * 2) + 3) * '-'}\n"

    for i in range((num * 2) + 1):  # 0-8
        if i != num:
            window += f"|{num * '.'}|{num * '.'}|\n"
        else:
            window += f"|{num * '-'}+{num * '-'}|\n"

    window += f"{((num * 2) + 3) * '-'}"

    return window


print(make_a_window_2(3))