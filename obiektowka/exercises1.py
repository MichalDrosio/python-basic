# def stock_info(company, country, price, currency):
#     return f"company:{company}\ncountry:{country}\nprice:{price}\ncurrency:{currency}"
#
# print(stock_info.__code__.co_varnames)
#
#
# array = [-4, 3, 2]
#
# import builtins
# help(builtins.sum)
# print(builtins.sum(array))
#
#
# counter = 1
#
#
# def update_counter():
#     global counter
#     counter += 1
#     print(counter)
#
# update_counter()
#
#
# counter_2 = 0
# dot_counter = ''
#
# def update_counter_2():
#     global counter_2, dot_counter
#     counter_2 += 1
#     dot_counter += '.'
#
#
# [update_counter_2() for i in range(40)]
# print(counter_2, dot_counter)


def display_info(number_of_updates=1):
    counter_3 = 100
    dot_counter_3 = ''

    def update_counter_3():
        nonlocal counter_3, dot_counter_3
        counter_3 += 1
        dot_counter_3 += '.'

    [update_counter_3() for _ in range(number_of_updates)]
    print(counter_3, dot_counter_3)

display_info(10)