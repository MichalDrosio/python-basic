# You and your friends have been battling it out with your Rock 'Em, Sock 'Em robots,
# but things have gotten a little boring. You've each decided to add some
# amazing new features to your robot and automate them to battle to the death.
#
# Each robot will be represented by an object. You will be given two robot objects,
# and an object of battle tactics and how much damage they produce. Each robot will have a name,
# hit points, speed, and then a list of battle tacitcs they are to perform in order.
# Whichever robot has the best speed, will attack first with one battle tactic.
#
# Your job is to decide who wins.
#
# Example:
# robot_1 = {
#     "name": "Rocky",
#     "health": 100,
#     "speed": 20,
#     "tactics": ["punch", "punch", "laser", "missile"]
# }
# robot_2 = {
#     "name": "Missile Bob",
#     "health": 100,
#     "speed": 21,
#     "tactics": ["missile", "missile", "missile", "missile"]
# }
# tactics = {
#     "punch": 20,
#     "laser": 30,
#     "missile": 35
# }
#
# fight(robot_1, robot_2, tactics) -> "Missile Bob has won the fight."
# robot2 uses the first tactic, "missile" because he has the most speed. This reduces robot1's health by 35.
# Now robot1 uses a punch, and so on.
#
# Rules
#
# A robot with the most speed attacks first. If they are tied, the first robot passed in attacks first.
# Robots alternate turns attacking. Tactics are used in order.
# A fight is over when a robot has 0 or less health or both robots have run out of tactics.
# A robot who has no tactics left does no more damage, but the other robot may use the rest of his tactics.
# If both robots run out of tactics, whoever has the most health wins. Return the message "{Name} has won the fight."
# If both robots run out of tactics and are tied for health, the fight is a draw. Return "The fight was a draw."

def fight(robot_1, robot_2, tactics):

    if robot_2['speed'] > robot_1['speed']:
        robot_first = robot_2
        robot_second = robot_1
    else:
        robot_first = robot_1
        robot_second = robot_2

    while ((len(robot_first['tactics']) > 0) or (len(robot_second['tactics']) > 0)):
        if len(robot_first['tactics']) > 0:
            robot_second['health'] -= tactics[robot_first['tactics'].pop(0)]
        if robot_second['health'] <= 0:
            return f"{robot_first['name']} has won the fight."

        if len(robot_second['tactics']) > 0:
            robot_first['health'] -= tactics[robot_second['tactics'].pop(0)]
        if robot_first['health'] <= 0:
            return f"{robot_second['name']} has won the fight."
    else:
        if robot_first['health'] == robot_second['health']:
            return "The fight was a draw."
        else:
            winner = robot_first['name'] if robot_first['health'] > robot_second['health'] else robot_second['name']
            return f'{winner} has won the fight.'



robot_1 = {
    "name": "Rocky",
    "health": 2000,
    "speed": 20,
    "tactics": ["punch", "punch", "laser", "missile"]
}
robot_2 = {
    "name": "Missile Bob",
    "health": 1000,
    "speed": 21,
    "tactics": ["missile", "missile", "missile", "missile"]
}
tactics = {
    "punch": 20,
    "laser": 30,
    "missile": 35
}

print(fight(robot_1, robot_2, tactics))

