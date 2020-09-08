# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to compute the distance from current position
# after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

start = [0, 0]

def movement(motion):
    while True:
        motion = input('kierunek ruchu: up, down, right, left, odlegość:\n')
        if not motion:
            break
        move = motion.split(' ')
        direction = move[0]
        step = int(move[1])

        if direction == 'up':
            start[0] += step
        elif direction == 'down':
            start[0] -= step
        elif direction == 'right':
            start[1] += step
        elif direction == 'left':
            start[1] -= step
        print(f'Aktualna pozycja to {start}')
    return start


def compute_the_distance_to_start():
    distance = movement(motion='motion')
    result =(distance[0]**2 + distance[1]**2) ** 0.5
    print(f'Odleglość od punktu startowego wynosi:{round(result)}')


compute_the_distance_to_start()


