#Given a tree, return its mirror
#    Before             After
#      0                  0
#     / \                / \
#    2   1              1   2
#   /   / \            / \   \
#  3   5   4          4   5   3


class Node():
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value


a = Node(0)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(4)
f = Node(5)

a.left = c
a.right = b
b.left = f
b.right = e
c.left = d

def invert(head):
    if head.left:
        invert(head.left)
    if head.right:
        invert(head.right)
    tmp = head.left
    head.left = head.right
    head.right = tmp

#Post-Order Traversal
def df_traverse(head):
    if head.left:
        df_traverse(head.left)
    if head.right:
        df_traverse(head.right)
    
    print(head.value)

#Pre-Order Traversal
def pre_order_df_traverse(head):
    print(head.value)
    if head.left:
        pre_order_df_traverse(head.left)
    if head.right:
        pre_order_df_traverse(head.right)

#In-Order Traversal
def in_order_df_traverse(head):
    if head.left:
        in_order_df_traverse(head.left)
    print(head.value)
    if head.right:
        in_order_df_traverse(head.right)
    

in_order_df_traverse(a)
invert(a)
in_order_df_traverse(a)