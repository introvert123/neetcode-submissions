# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def dfs(root,result):
            if root:
                dfs(root.left, result)
                dfs(root.right, result)
                result.append(root.val)

        dfs(root,result)
        return result
        