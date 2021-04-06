# Johnny is a farmer and he annually holds a beet farmers convention "Drop the beet".
#
# Every year he takes photos of farmers handshaking. Johnny knows that no two farmers handshake more than once.
# He also knows that some of the possible handshake combinations may not happen.
#
# However,
# Johnny would like to know the minimal amount of people that participated this year just by counting
# all the handshakes.
#
# Help Johnny by writing a function, that takes the amount of handshakes and
# returns the minimal amount of people needed to perform these handshakes (a pair of farmers handshake only once).

def get_participants(handshakes):
    n = 0
    counter = 0
    while handshakes > 0:
        handshakes -= counter
        n += 1
        counter += 1
    return n or 1


print(get_participants(0))
print(get_participants(1))
print(get_participants(3))
print(get_participants(5))
print(get_participants(10))