class Node():
    parent, left, right = None, None, None

    def __init__(self, parent, left, right) -> None:
        self.parent = parent
        self.left = left
        self.right = right

def rotate_left(problem_node_grandparent):
    new_grandparent = problem_node_grandparent.right
    problem_node_grandparent.right = new_grandparent.left
    new_grandparent.left = problem_node_grandparent
    return new_grandparent

def rotate_right(problem_node_grandparent):
    new_grandparent = problem_node_grandparent.left
    problem_node_grandparent.left = new_grandparent.right
    new_grandparent.right = problem_node_grandparent
    return new_grandparent

def rotate_right_left(problem_node_grandparent):
    problem_node_grandparent.right = rotate_right(problem_node_grandparent.right)
    return rotate_left(problem_node_grandparent)

def rotate_left_right(problem_node_grandparent):
    problem_node_grandparent.left = rotate_left(problem_node_grandparent.left)
    return rotate_right(problem_node_grandparent)