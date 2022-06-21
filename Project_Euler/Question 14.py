def collatz(value):
    current = value
    counter = 1
    while current != 1:
        if current % 2 == 0:
            current /= 2
        else:
            current = current * 3 + 1
        counter += 1
    return (counter, value)

print(max(map(collatz, (i for i in range(1, 1000000)))))

