# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
#
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
account = 0


while True:
    transaction = input('wybierz operacje:(wp-wplata, wy-wyplata) srodkow\n')
    value = int(input('wartosc'))
    if transaction =='wp':
        account += value
        print(f'wplata:{value}')
    elif transaction == 'wy':
        if value <= account:
            account -= value
            print(f'wyplata:{value}')
        else:

            print(f'brak wystarczajacych srodkow, na koncie jest:{account}, chciales wyplacic:{value} ')
    print(f'aktualny stan konta:{account}')

