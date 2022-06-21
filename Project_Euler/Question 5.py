def func():
    cur = 2520
    while(True):
        result = cur
        for i in range(1, 21):
            if cur % i != 0:
                cur += 1
        if result == cur:
            return result
    
print(func())