# Your granny, who lives in town X0, has friends. These friends are given in an array, for example: array of friends is
#
# [ "A1", "A2", "A3", "A4", "A5" ].
# The order of friends is this array must not be changed since this order gives the order in which they will be visited.
#
# These friends inhabit towns and you have an array with friends and towns, for example:
#
# [ ["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"] ]
# or
# [ ("A1", "X1"), ("A2", "X2"), ("A3", "X3"), ("A4", "X4") ]
# or
# (C)
# {"A1", "X1", "A2", "X2", "A3", "X3", "A4", "X4"}
# which means A1 is in town X1, A2 in town X2... It can happen that we don't know the town of one of the friends.
#
# Your granny wants to visit her friends and to know how many miles she will have to travel.
#
# You will make the circuit that permits her to visit her friends. For example here the circuit will contain:
#
# X0, X1, X2, X3, X4, X0
# and you must compute the total distance
#
# X0X1 + X1X2 + .. + X4X0.
# For the distance, fortunately, you have a map (and a hashmap) that gives each distance X0X1, X0X2 and so on.
# For example:
#
# [ ["X1", 100.0], ["X2", 200.0], ["X3", 250.0], ["X4", 300.0] ]
# or
# Map("X1" -> 100.0, "X2" -> 200.0, "X3" -> 250.0, "X4" -> 300.0)
# or (Coffeescript, Javascript)
# ['X1',100.0, 'X2',200.0, 'X3',250.0, 'X4',300.0 ]
# or
# (C)
# {"X1", "100.0", "X2", "200.0", "X3", "250.0", "X4", "300.0"}
friends1 = ('A1', 'A2', 'A3', 'A4', 'A5')
fTowns1 = [['A1', 'X1'], ['A2', 'X2'], ['A3', 'X3'], ['A4', 'X4']]
distTable1 = {'X1': 100.0, 'X2': 200.0, 'X3': 250.0, 'X4': 300}

def tour(friends, friend_towns, home_to_town_distance):
    result = 0
    s = 0
    for index in friend_towns:
        print(f'index: {index}')
        if index[0] in friends:
            print(f'result;{result}')
            print(f'({home_to_town_distance[index[1]]**2}-{s**2})**{0.5}=={(home_to_town_distance[index[1]]**2-s**2)**(0.5)}')
            result = result + (home_to_town_distance[index[1]]**2-s**2)**(0.5)
            print(f'{index[0]}|||| {result} + {(home_to_town_distance[index[1]]**2-s**2)**(0.5)}=={result + (home_to_town_distance[index[1]]**2-s**2)**(0.5)}')
            s = home_to_town_distance[index[1]]
            print(f'{s} =={home_to_town_distance[index[1]]}')
    result += s
    return int(result)




print(tour(friends=friends1, friend_towns=fTowns1, home_to_town_distance=distTable1))

# a = 100.0
# b = 200.0
# if c < a+b:
#     c< 300
# if b<a+c:
#     c>100
# if a<b+c:
#     c>-100

