val = 600851475143
i = 2
while i < val:
    if val % i == 0:
        val = val / i
        i = 2
    else:
        i += 1

print(val)