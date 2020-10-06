import string

template1 = string.Template(' $x ma kota $y')

dictionary = {'x': 'michal', 'y': 'nala'}

print(template1.substitute(dictionary))

students_array = [('ola', 20), ('michal', '25'), ('magda', 30)]
template2 = string.Template('$x otrzymal $y punktow na egzaminie')

for i in students_array:
    print(template2.substitute(x=i[0], y=i[1]))

products_array = [{'name': 'woda', 'price': 2, 'quantity': '6'}, {'name': 'bulki', 'price': 1.5, 'quantity': 6},
                  {'name': 'pomidory', 'price': 2.5, 'quantity': 4}]

template3 = string.Template('dodales do koszyka $quantity prodoktow $name w cenie $price za sztuke')

for i in products_array:
    print(template3.substitute(i))
