from collections import deque


graph = {'a':['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e':[], 'f':[]}

#recursive
def depth_first_traverse(head):
    result = []
    result.append(head)
    for item in graph[head]:
        result += depth_first_traverse(item)
    return result
    

#iterative
def DFT_iterative(head):
    my_stack = deque()
    my_stack.append(head)
    while my_stack:
        cur = my_stack.pop()
        print(cur)
        for item in graph[cur][::-1]:
            my_stack.append(item)


# print(depth_first_traverse('a'))
DFT_iterative('a')
