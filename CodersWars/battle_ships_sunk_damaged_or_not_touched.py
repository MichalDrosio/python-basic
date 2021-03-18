# Your task in the kata is to determine how many boats are sunk damaged and untouched from a set amount of attacks.
# You will need to create a function that takes two arguments, the playing board and the attacks.
# Boats are placed either horizontally, vertically or diagonally on the board.
# 0 represents a space not occupied by a boat. Digits 1-3 represent boats which vary in length 1-4 spaces long.
# There will always be at least 1 boat up to a maximum of 3 in any one game.
# Boat sizes and board dimentions will vary from game to game.
#
# Attacks
# Attacks are calculated from the bottom left, first the X coordinate then the Y.
# There will be at least one attack per game, and the array will not contain duplicates.
#
# [[2, 1], [1, 3], [4, 2]]
# First attack      `[2, 1]` = `3`
# Second attack `[1, 3]` = `0`
# Third attack     `[4, 2]` = `1`
# Function Initialization
# board = [[0,0,0,2,2,0],
#          [0,3,0,0,0,0],
#          [0,3,0,1,0,0],
#          [0,3,0,1,0,0]]
# attacks = [[2, 1], [1, 3], [4, 2]]
# damaged_or_sunk(board, attacks)

def damaged_or_sunk(board, attacks):
    game_result = {'sunk': 0, 'damaged': 0, 'points': 0, 'not_touched': 0}
    for attack in range(len(attacks)):
        x = attacks[attack][1]
        y = attacks[attack][0]
        line_x = board[x]
        print(line_x)
        hit_or_miss = line_x[y-1]
        print(line_x[y-1])
        if hit_or_miss == 0:
            print('pudlo')
        elif hit_or_miss == 1:
            print('trafiony zatopiony')
            game_result['sunk'] += 1
            game_result['points'] += 1
        else:
            print('trafiony')
            game_result['points'] += 0.5

    return game_result



board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,2],
         [0,3,0,1,0,0]]

attacks = [[4, 2]]
print(damaged_or_sunk(board,attacks))
c=[ [1, 3], [4, 2]]