# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        if root:
            self.traverse(root, result) 
        
        return result[k-1]

    def traverse(self, root: Optional[TreeNode], result):
        if root:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)
