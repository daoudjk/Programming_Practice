import math
primes = [2, 3, 5, 7, 11, 13]
tmp = 15
# root = math.sqrt(tmp)
while(len(primes) < 10001):
    nextVal = tmp
    for i in primes:
        # if tmp % i == 0 or i > root:
        if tmp % i == 0:
            tmp += 2
            # root = math.sqrt(tmp)
            break
    if nextVal == tmp:
        primes.append(nextVal)
        
        
print(primes[-1])
