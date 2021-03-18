# Write a function dirReduc which will take an array of strings and returns an array of strings
# with the needless directions removed (W<->E or S<->N side by side).
#
# The Haskell version takes a list of directions with data Direction = North | East | West | South.
# The Clojure version returns nil when the path is reduced to nothing.
# The Rust version takes a slice of enum Direction {North, East, West, South}.
# See more examples in "Sample Tests:"
# Notes
# Not all paths can be made simpler. The path ["NORTH", "WEST", "SOUTH", "EAST"] is not reducible.
# "NORTH" and "WEST", "WEST" and "SOUTH", "SOUTH" and "EAST" are not directly opposite of each other
# and can't become such. Hence the result path is itself : ["NORTH", "WEST", "SOUTH", "EAST"].
opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dir_reduc(array):
    new_array = []
    for dire in array:
        if new_array and new_array[-1] == opposite[dire]:
            new_array.pop()
        else:
            new_array.append(dire)
    return new_array


array = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dir_reduc(array))

