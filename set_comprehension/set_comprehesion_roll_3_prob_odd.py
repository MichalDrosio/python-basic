roll = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
print(roll)
roll_odd = {(x, y, z) for x, y, z in roll if x % 2!= 0 and y % 2!= 0 and z % 2!= 0}
print(roll_odd)
prob = round(len(roll_odd) / len(roll), 3)
print(prob)