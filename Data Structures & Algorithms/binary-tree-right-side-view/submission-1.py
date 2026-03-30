# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            r = None
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    r = node.val
                    q.append(node.left)
                    q.append(node.right)
            if r:
                res.append(r)
        return res
            
        


        