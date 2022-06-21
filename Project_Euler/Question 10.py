import math
primes = [2, 3, 5, 7, 11, 13]
tmp = 15
root = (int)(math.sqrt(tmp))+1
while(primes[-1] < 2000000):
    nextVal = tmp
    for i in primes:
        if i > root:
            break
        if tmp % i == 0:
            tmp += 2
            root = (int)(math.sqrt(tmp))+1
            break
    if nextVal == tmp:
        primes.append(nextVal)
        tmp += 2
        root = (int)(math.sqrt(tmp))+1
    if len(primes) % 1000 == 0:
        print(primes[-1])
        
        
primes.pop()
print(sum(primes))
