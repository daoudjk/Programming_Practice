from re import I


def generate_triangular_number(n):
    return sum(i for i in range(1, n+1))


# Sieve of eratosthenes from: https://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
def generate_prime():
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        print("q " + str(q))
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                print("p " + str(p))
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def get_factors(n):
    result = set()
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n//i)
    return result

triangular_number = 0
i = 1
while len(get_factors(triangular_number)) <= 500:
    triangular_number += i
    i += 1

print(triangular_number)
