probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = [i for i in probabilities if i > 0.5]

print(result)
res = [1 if i > 0.5 else 0 for i in probabilities]
print(res)