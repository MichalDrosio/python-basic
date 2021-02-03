# Modify the kebabize function so that it converts a camel case string into a kebab case.
#
# kebabize('camelsHaveThreeHumps') // camels-have-three-humps
# kebabize('camelsHave3Humps') // camels-have-humps
# Notes:
#
# the returned string should only contain lowercase letters

def kebabize(string):
    result = ''
    for i in string:
        if i.isupper():
            if result is not '':
                result += f'-{i.lower()}'
            else:
                result += i.lower()
        if i.islower():
            result += i
    return result

print(kebabize('camelsHaveThreeHumps'))
print(kebabize('myCamelHas3Humps'))

