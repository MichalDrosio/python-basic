# Clients place orders to a stockbroker as strings. The order can be simple or multiple or empty.
#
# Type of a simple order: Quote/white-space/Quantity/white-space/Price/white-space/Status
#
# where Quote is formed of non-whitespace character, Quantity is an int,
# Price a double (with mandatory decimal point "." ),
# Status is represented by the letter B (buy) or the letter S (sell).
#
# Example:
# "GOOG 300 542.0 B"
#
# A multiple order is the concatenation of simple orders with a comma between each.
#
# Example:
# "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"
#
# or
#
# "ZNGA 1300 2.66 B,CLH15.NYM 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"
#
# To ease the stockbroker your task is to produce a string of type
#
# "Buy: b Sell: s" where b and s are 'double' formatted with no decimal,
# b representing the total price of bought stocks and s the total price of sold stocks.
#
# Example:
# "Buy: 294990 Sell: 0"
#
# Unfortunately sometimes clients make mistakes.
# When you find mistakes in orders, you must pinpoint these badly formed orders and produce a string of type:
#
# "Buy: b Sell: s; Badly formed nb: badly-formed 1st simple order ;badly-formed nth simple order ;"
#
# where nb is the number of badly formed simple orders,
# b representing the total price of bought stocks with correct simple order and s
# the total price of sold stocks with correct simple order.
#
# Examples:
# "Buy: 263 Sell: 11802; Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;"
#
# "Buy: 100 Sell: 56041; Badly formed 1: ZNGA 1300 2.66 ;"
#
# Notes:
# If the order is empty, Buy is 0 and Sell is 0 hence the return is: "Buy: 0 Sell: 0".
# Due to Codewars whitespace differences will not always show up in test results.
# With Golang (and maybe others) you can use a format with "%.0f" for "Buy" and "Sell".

def balance_statement(lst):
    array = lst.split(',')
    buy = 0
    sell = 0
    error = []
    if lst == '':
        return f'Buy: {buy} Sell: {sell}'
    else:
        for item in array:
            i = item[:-2].rstrip('1234567890.').rstrip()
            cash = item[len(i):-2]
            try:
                cash = int(item[len(i):-2])
                error.append(item.lstrip())
            except ValueError:
                count = i[len(i.strip().rstrip('1234567890')):]
                if item[-1] == 'B':
                    buy += float(cash) * int(count.strip())
                elif item[-1] == 'S':
                    sell += float(cash) * int(count.strip())
                else:
                    error.append(item.lstrip())
        if error == []:
            return f"Buy: {round(buy)} Sell: {round(sell)}"
        else:
            return f"Buy: {round(buy)} Sell: {round(sell)}; Badly formed {len(error)}: {' ;'.join(error)} ;"


print(balance_statement("GOOG 90.1 160.45 B, JPMC 67 12.8 S, MYSPACE 24.0 210 B, CITI 50 450 B, CSCO 100 55.5 S"))
# print(balance_statement("ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, OGG 20 580.1 B"))
# print(balance_statement(''))
# print(balance_statement("ZNGA 1300 2.66, CLH15.NYM 50 56.32 S, OWW 1000 11.623 S, OGG 20 580.1 S"))