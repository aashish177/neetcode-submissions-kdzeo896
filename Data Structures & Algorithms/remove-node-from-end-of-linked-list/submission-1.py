# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initialize node to head
        # iterate until node is not None
        # count += 1 every iteration
        # removeNode = count - n
        # for _ in range(remove node):
        # curr = curr.next
        # prev = curr
        # curr = curr.next
        # temp = curr.next
        # prev.next = temp
        # curr.next = None

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        removeNode = len(nodes) - n

        if removeNode == 0:
            return head.next

        nodes[removeNode - 1].next = nodes[removeNode].next

        return head
        