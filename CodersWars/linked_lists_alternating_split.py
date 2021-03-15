# Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists.
# The sublists should be made from alternating elements in the original list. So if the original
# list is a -> b -> a -> b -> a -> null then one sublist should be a -> a -> a -> null and the other should be b - null
# list = 1 -> 2 -> 3 -> 4 -> 5 -> None
# alternating_split(list).first == 1 -> 3 -> 5 -> None
# alternating_split(list).second == 2 -> 4 -> None

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError('Bad input')

    orig_a, orig_b = a, b = Node(), Node()

    while head:
        a.next = Node(head.data)
        a, b = b, a
        head = head.next
    return Context(orig_a.next, orig_b.next)

print(alternating_split.first([1,2,3,4,5]))