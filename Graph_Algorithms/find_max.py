#given a potentially disjoint graph of nodes, find the largesst component
#need to traverse all nodes, keep track of visited nodes in a set of some sort

graph = {0: [8, 1, 5], 1: [0], 5:[0, 8], 8:[0, 5], 2: [3, 4], 3: [2, 4], 4: [3,2]}
# graph = {0: []}

def find_max(node, visited):
    if node in visited:
        return node
    result = node
    visited.add(node)
    for item in graph[node]:
        max_value = find_max(item, visited)
        if max_value > result:
            result = item
    return result


def wrapper(graph):
    if graph is None:
        return None
    
    # if len(graph) == 1:
    #     return graph[0]

    largest = int()
    visited = set()

    for item in graph:
        if item not in visited:
            max_value = find_max(item, visited)
            if max_value > largest:
                largest = max_value
    return largest

print(wrapper(graph))