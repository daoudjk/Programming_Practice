#Given a number n, print n-th Fibonacci Number. 

number = 300

def nth_fib(n, memo):
    if n in memo:
        return memo[n]
    else:
        memo[n] = nth_fib(n-1, memo) + nth_fib(n-2, memo)
        return memo[n]

my_cache = {}
my_cache[0] = 0
my_cache[1] = 1
print(nth_fib(number, my_cache))