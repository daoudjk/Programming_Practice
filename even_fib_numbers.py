val1 = 1
val2 = 1
sum = 0

while(val1 < 4000000):
    newVal = val1+val2
    if newVal % 2 == 0 and newVal < 4000000:
        sum += newVal
    val2 = val1
    val1 = newVal

print(sum)