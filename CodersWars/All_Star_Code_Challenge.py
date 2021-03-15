# ou work for an ad agency and your boss, Bob, loves a catchy slogan.
# He's always jumbling together "buzz" words until he gets one he likes.
# You're looking to impress Boss Bob with a function that can do his job for him.
#
# Create a function called sloganMaker() that accepts an array of string "buzz" words.
# The function returns an array of all possible UNIQUE string permutations of the buzz words
# (concatonated and separated by spaces).
#
# Your boss is not very bright, so anticipate him using the same "buzz" word more than once, by accident.
# The function should ignore these duplicate string inputs.
#
# sloganMaker(["super", "hot", "guacamole"]);
# //[ 'super hot guacamole',
# //  'super guacamole hot',
# //  'hot super guacamole',
# //  'hot guacamole super',
# //  'guacamole super hot',
# //  'guacamole hot super' ]
#
# sloganMaker(["cool", "pizza", "cool"]); // => [ 'cool pizza', 'pizza cool' ]

from itertools import permutations
array = ["super", "hot", "guacamole", 'super']


def slogan_maker(array):
    array_with_out_duplicate = []
    for i in array:
        if i not in array_with_out_duplicate:
            array_with_out_duplicate.append(i)

    array = [' '.join(element) for element in list(permutations(array_with_out_duplicate, len(array_with_out_duplicate)))]
    return array


print(slogan_maker(array))


