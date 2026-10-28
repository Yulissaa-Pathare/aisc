inputs = [[0,0], [0,1], [1,0], [1,1]]
targets = [0, 0, 0, 1]

w1 = 0.0
w2 = 0.0
bias = 0.0
lr = 0.1

for epoch in range(1000):
    for i in range(4):
        x1, x2 = inputs[i]

        output = w1*x1 + w2*x2 + bias
        error = targets[i] - output

        w1 = w1 + lr*error*x1
        w2 = w2 + lr*error*x2
        bias = bias + lr*error

print("Final weights:", round(w1, 2), round(w2, 2))
print("Final bias:", round(bias, 2))

print("AND Gate Output:")
for x1, x2 in inputs:
    output = w1*x1 + w2*x2 + bias
    prediction = 1 if output >= 0.5 else 0
    print(x1, x2, "=", prediction)