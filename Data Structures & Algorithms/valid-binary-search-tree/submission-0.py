# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidSubtree(root, float('-inf'), float('inf'))
        

    def isValidSubtree(self, root: Optional[TreeNode], minValue: int, maxValue: int):

        if not root:
            return True

        if minValue < root.val < maxValue and self.isValidSubtree(root.left, minValue, root.val) and self.isValidSubtree(root.right, root.val, maxValue):
            return True
        else:
            return False


        