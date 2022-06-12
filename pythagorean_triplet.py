import math
result = 0
val1 = 2
val2 = 3
val3 = 0
while result != 1000:
    val3 = math.sqrt(val1 * val1 + val2 * val2)
    result = val1+val2+val3
    if result < 1000:
        val1 += 1
        val2 += 1
    elif result > 1000:
        val1 -= 1
print(val1*val2*val3)