# A Discovery
# While turning through the fields one fine day with his favorite rotary plough,
# farmer Arepo struck upon something quite odd: a square stone tablet with strange symbols carved into it...
# he knew some such objects could portray the same message in four different directions all at once,
# so he wisely kept it for later examination and dutifully resumed working the rich soil. As he wheeled on,
# he found more such tablets, but with so many crops to sow, he had no time for deciphering their many glyphs.
#
# Your Task
# Please help Arepo by reading each tablet to discern whether or not it is a Sator Square!
#
# The Square . . .
# is known as a two-dimentional palindrome observing four symmetries
#
# can be read:
#
# top-to-bottom
# bottom-to-top
# left-to-right
# right-to-left
# may be rotated 180 degrees and still be read in all four ways
#
# is shown here illustrates how you can read the word "TUBA" in four different directions:
#
#           v
#       B A T S
#       A B U T <
#     > T U B A
#       S T A B
#         ^
# ...and every word in the square can be thus read!
#
# Input
# tablet  #  a 2D char list (2 <= n <= 33)
# Output
# True / False  #  whether or not the tablet is a sator square


def is_sator_square(tablet):
    return tablet == [t[::-1] for t in tablet][::-1] == list(map(list, zip(*tablet)))



tablet = [['S', 'T', 'A', 'B'],
          ['T', 'U', 'B', 'A'],
          ['A', 'B', 'U', 'T'],
          ['B', 'A', 'T', 'S']]

tablet2 = [['K', 'N', 'I', 'T'],
          ['N', 'O', 'R', 'I'],
          ['I', 'R', '0', 'N'],
          ['T', 'I', 'N', 'K']]

print(is_sator_square(tablet))
print(is_sator_square(tablet2))