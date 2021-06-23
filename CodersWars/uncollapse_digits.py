# You will be given a string of English digits "stuck" together, like this:
#
# "zeronineoneoneeighttwoseventhreesixfourtwofive"
#
# Your task is to split the string into separate digits:
#
# "zero nine one one eight two seven three six four two five"
#
# Examples
# "three"              -->  "three"
# "eightsix"           -->  "eight six"
# "fivefourseven"      -->  "five four seven"
# "ninethreesixthree"  -->  "nine three six three"
# "fivethreefivesixthreenineonesevenoneeight"  -->  "five three five six three nine one seven one eight"

def uncollapse(digits):
    array = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = []
    i = 0
    number = ''
    while i < len(digits):
        number += digits[i]
        if number in array:
            result.append(number)
            number = ''
        i += 1
    print(result)
    return ' '.join(result)


print(uncollapse("fivethreefivesixthreenineonesevenoneeight"))