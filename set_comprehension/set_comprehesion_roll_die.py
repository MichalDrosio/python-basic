x = {(i, j) for i in range(1, 7) for j in range(1, 7)}
print(x)

sum_gt_10 = {pair for pair in x if pair[0] + pair[1] >= 10}

print(sum_gt_10)
print(len(sum_gt_10)/len(x))