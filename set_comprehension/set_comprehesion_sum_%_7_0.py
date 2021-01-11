roll = {(x, y, z) for x in range(1, 7) for y in range(1, 7) for z in range(1, 7)}
print(roll)
sum_div_by_7 = {(x, y, z) for x, y, z in roll if (x + y + z) % 7 == 0}
print(sum_div_by_7)
prob = round(len(sum_div_by_7) / len(roll), 2)
print(prob)