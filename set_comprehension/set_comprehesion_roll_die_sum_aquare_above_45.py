roll = {(x, y) for x in range(1, 7) for y in range(1, 7)}
print(roll)
roll_above_45 = {(x, y) for x, y in roll if x**2 + y**2 >= 45}
print(roll_above_45)
prob = round(len(roll_above_45) / len(roll), 2)
print(prob)