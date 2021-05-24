# You must create a method that can convert a string from any format into PascalCase.
# This must support symbols too.
#
# Don't presume the separators too much or you could be surprised.
#
# For example: (Input --> Output)
#
# "example name" --> "ExampleName"
# "your-NaMe-here" --> "YourNameHere"
# "testing ABC" --> "TestingAbc"

def camelize(str_):
    result = ''
    new_word = True
    for elem in str_:
        if elem.isalnum():
            if new_word:
                result += elem.upper()
            else:
                 result += elem.lower()
            new_word = False
        else:
            new_word = True
    return result

# print(camelize('KqfZapufgwx2GblkrofZ'))
# print(camelize("cODE warS"))
# print(camelize('tVU77TBewGcg2csB'))
# print(camelize("'Quoted'=>'What'"))
print(camelize('Rugby:Club:2013'))
# print(camelize('Arabian_String-Test'))
# print(camelize('Ninja-Test--01'))