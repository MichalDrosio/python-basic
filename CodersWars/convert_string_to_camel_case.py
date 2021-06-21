# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
# The first word within the output should be capitalized only if the original word was capitalized
# (known as Upper Camel Case, also often referred to as Pascal case).
#
# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"


def to_camel_case(text):
    if not text:
        return "An empty string was provided but not returned"
    else:
        text = text.replace('-', ',').replace('_', ',')
        text = text.split(',')
        result = ''
        for i in text:
            if result:
                result += i.title()
            else:
                result += i
        return result

print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))
print(to_camel_case('A-B-C'))