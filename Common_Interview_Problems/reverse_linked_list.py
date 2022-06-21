#Probelm: Given the head of a linked list, return the linked list, reversed

from multiprocessing.sharedctypes import Value


class Node():
    def __init__(self, next=None, value=0):
        self.next = next
        self.value = value


a = Node(value='a')
b = Node(value='b')
c = Node(value='c')
d = Node(value='d')
a.next = b
b.next = c
c.next = d


def reverse(head):
    if head is None or head.next is None:
        return head
    result = reverse(head.next)
    head.next.next = head
    head.next = None

    return result

head = a
cur = head
while cur is not None:
    print(cur.value)
    cur = cur.next
head = reverse(a)
cur = head
while cur is not None:
    print(cur.value)
    cur = cur.next