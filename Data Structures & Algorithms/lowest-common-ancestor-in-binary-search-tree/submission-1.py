# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # ancestorP = []
        # ancestorQ = []
        # aP = []
        # aQ = []

        # stackP = [root]
        # stackQ = [root]
        # while True:
        #     node = stackP.pop()
        #     value = node.val
        #     ancestorP.append(node)
        #     aP.append(node.val)
        #     if p.val == value:
        #         break
        #     if p.val > value:
        #         stackP.append(node.right)
        #     else:
        #         stackP.append(node.left)
        
        # while True:
        #     node = stackQ.pop()
        #     value = node.val
        #     ancestorQ.append(node)
        #     aQ.append(node.val)
        #     if q.val == value:
        #         break
        #     if q.val > value:
        #         stackQ.append(node.right)
        #     else:
        #         stackQ.append(node.left)


        # return p

        if not root or not p or not q:
            return None
        
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root