class Node:
    """Class used to create linked list"""

    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    def __str__(self):
        return str(self.value)


def nth_from_last(head, n):
    """Returns n-th element from linked list, counting from the end"""

    start = head
    end = head

    for i in range(n):
        if end == None:
            return None
        end = end.child

    while end:
        end = end.child
        start = start.child

    return str(start)


def nth_from_last_naive(head, n):
    """ NAIVE approach, not recommended.
    It uses much more memory to store each element with its index.
    Returns n-th element from linked list, counting from the end"""

    if not head:
        return None
        
    storage = []
    current = head
    while current:
        storage.append(str(current.value))
        current = current.child

    if n > len(storage):
        return None

    return storage[len(storage) - n]
