#Do not use recursion in BFS because you'll be using the call stack which will inherently work against you
#the behavior we want for BFS is more like a queue than a stack

from collections import deque


graph = {'a':['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e':[], 'f':[]}

def BFT(head):
    results = deque()
    results.append(head)
    while results:
        cur = results.popleft()
        print(cur)
        for item in graph[cur]:
            results.append(item)

BFT('a')