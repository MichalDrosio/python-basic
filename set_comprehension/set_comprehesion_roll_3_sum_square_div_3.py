roll = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
print(roll)

roll_sum_square_div_by_3 = {(x, y, z) for x, y, z in roll if (x**2 + y**2 + z**2) % 3 == 0}
print(roll_sum_square_div_by_3)
prob = round(len(roll_sum_square_div_by_3) / len(roll), 4)
print(prob)