import math

data = [[1, 1], [1, 0], [0, 1], [0, 0], [0.9, 0.8]]

weights = [[0.2, 0.3], [0.8, 0.7]]
lr = 0.5

for epoch in range(100):
    for x in data:
        d1 = math.sqrt((x[0]-weights[0][0])**2 +
                       (x[1]-weights[0][1])**2)
        d2 = math.sqrt((x[0]-weights[1][0])**2 +
                       (x[1]-weights[1][1])**2)

        if d1 < d2:
            winner = 0
        else:
            winner = 1

        for i in range(2):
            weights[winner][i] += lr * (x[i] - weights[winner][i])

    lr *= 0.99

print("Final Weights:", weights)
print("Cluster Assignments:")

for x in data:
    d1 = math.sqrt((x[0]-weights[0][0])**2 +
                   (x[1]-weights[0][1])**2)
    d2 = math.sqrt((x[0]-weights[1][0])**2 +
                   (x[1]-weights[1][1])**2)

    if d1 < d2:
        print(x, "-> Cluster 1")
    else:
        print(x, "-> Cluster 2")