# Finding your seat on a plane is never fun, particularly for a long haul flight...
# You arrive, realise again just how little leg room you get,
# and sort of climb into the seat covered in a pile of your own stuff.
#
#
# the naming system consists of a number (in this case between 1-60) that denotes the section of the plane
# where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter,
# A-K with the exclusions mentioned above.
#
# Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.
#
# Given a seat number, your task is to return the seat location in the following format:
#
# '2B' would return 'Front-Left'.
#
# If the number is over 60, or the letter is not valid, return 'No Seat!!'.
import string
def plane_seat(a):
    section = ('ABC', 'DEF', 'GHI')
    letter = a[-1]
    num = a[:-1]
    side = ''
    direction = ''

    if letter in string.ascii_uppercase[9:] or int(num) > 60:
        return 'No Seat!'
    else:
        if letter in section[0]:
            side += "Left"
        elif letter in section[1]:
            side += "Middle"
        elif letter in section[2]:
            side += "Right"
        if int(num) in range(1, 21):
            direction += 'front'
        elif int(num) in range(21, 41):
            direction += 'middle'
        else:
            direction += 'back'
        return f'{side}-{direction}'


print(plane_seat('20B'))
print(plane_seat('21B'))
print(plane_seat('40B'))
print(plane_seat('41B'))
print(plane_seat('60B'))
print('=========================')
print(plane_seat('61B'))
print(plane_seat('20L'))
print(plane_seat('20L'))
print(plane_seat('17K'))



