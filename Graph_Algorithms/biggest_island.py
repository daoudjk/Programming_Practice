#given a disjoint graph of nodes, find the largesst "island"
#need to traverse all nodes, keep track of visited nodes in a set of some sort

graph = {0: [8, 1, 5], 1: [0], 5:[0, 8], 8:[0, 5], 2: [3, 4], 3: [2, 4], 4: [3,2]}


def helper(node, visited):
    result = 1
    for item in graph[node]:
        if item not in visited:
            visited.add(item)
            result += helper(item, visited)
    return result

def find_biggest_island(graph):
    if graph is None:
        return None
    biggest_island_size = int()
    visited = set()
    for item in graph:
        visited.add(item)
        result = helper(item, visited)
        if result > biggest_island_size:
            biggest_island_size = result
    return biggest_island_size

print(find_biggest_island(graph))
