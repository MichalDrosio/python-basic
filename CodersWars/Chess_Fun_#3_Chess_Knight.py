# Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.
#
# The knight can move to a square that is two squares horizontally and one square vertically,
# or two squares vertically and one square horizontally away from it.
# The complete move therefore looks like the letter L.
# Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.


def chess_knight(cell):
    x = '0abcdefgh'.index(cell[0])
    y = int(cell[1])
    jumps = [-2, -1, 1, 2,]
    counter = 0
    for i in jumps:
        for j in jumps:
            if abs(i) != abs(j) and x + i >= 1 and x + i <= 8 and y + j >= 1 and y + j <= 8:
                counter += 1
    return counter

def chess_knight2(cell):
    lookup = {2: ('a1', 'a8', 'h1', 'h8'),
              3: ('a2', 'b1', 'a7', 'b8', 'g1', 'h2', 'g8', 'h7'),
              4: ('b2', 'b7', 'g2', 'g7', 'c1', 'd1', 'e1', 'f1', 'c8', 'd8', 'e8', 'f8', 'a3', 'a4', 'a5', 'a6', 'h3', 'h4', 'h5', 'h6'),
              6: ('c2', 'd2', 'e2', 'f2', 'c7', 'd7', 'e7', 'f7', 'b3', 'b4', 'b5', 'b6', 'g3', 'g4', 'g5', 'g6'),
              8: ('c3', 'c4', 'c5', 'c6', 'd3', 'd4', 'd5', 'd6', 'e3', 'e4', 'e5', 'e6', 'f3', 'f4', 'f5', 'f6')
             }
    try:
        return [i[0] for i in lookup.items() if cell in i[1]][0]
    except:
        return 'please input a valid cell'


print(chess_knight2('c3'))