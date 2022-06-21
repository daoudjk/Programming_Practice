#Given a graph, return the path from head to some target node if such a path exists. Otherwise return None
#this is a depth first search problem

#recurse down the graph. If we reach the end of a path, and we do not find the result, return an empty list
#if we do find the result, return the key

graph = {'a':['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e':['g'], 'f':[], 'g': []}
# graph = {}

target = 'g'

def find_path(node, goal):
    result = []
    if not node in graph:
        return None
    for i in graph[node]:
        if i == goal:
            result += node
            result += i
            return result
        else:
            rest_of_path = find_path(i, goal)
            if rest_of_path:
                result += node
                result += rest_of_path
    return result

print(find_path('a', 'g'))