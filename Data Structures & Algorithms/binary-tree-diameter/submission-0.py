# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def height(self, root):
        if not root:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftD = self.height(root.left)
        rightD = self.height(root.right)
        totalHeight = leftD + rightD

        sub = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        maxH = max(totalHeight, sub)
        return maxH

