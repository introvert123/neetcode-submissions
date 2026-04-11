# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))