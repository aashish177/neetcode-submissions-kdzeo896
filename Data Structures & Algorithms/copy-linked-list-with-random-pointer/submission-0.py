"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        oldToCopy = {None:None}

        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        node = head
        while node:
            copy = oldToCopy[node]
            copy.next = oldToCopy[node.next]
            copy.random = oldToCopy[node.random]
            node = node.next
        return oldToCopy[head]