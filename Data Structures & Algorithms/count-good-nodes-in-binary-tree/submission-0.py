# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.count = 0
        
        def path(node, maxValue):
            
            if node:
                if node.val >= maxValue:
                    self.count += 1
                    maxValue = node.val

                path(node.left, maxValue)
                path(node.right, maxValue)
            else:
                return


        path(root, float('-inf'))
        return self.count
        