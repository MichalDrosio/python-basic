y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]


def accuracy(true, pred):
    counter = 0
    for i, j in zip(true, pred):
        if i == j:
            counter += 1
    return round(counter / len(true), 4)


print(accuracy(y_true, y_pred))