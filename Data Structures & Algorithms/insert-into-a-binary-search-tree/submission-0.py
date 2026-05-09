# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        newNode = TreeNode(val)
        parent = self.insertAt(None, root)
        if not parent:
            return newNode
        elif parent.val < val:
            parent.right = newNode
        else:
            parent.left = newNode

        return root

    def insertAt(self, parent, node):
        if not node:
            return parent
        
        if node.val < val:
            return self.insertAt(node, node.right)
        else:
            return self.insertAt(node, node.left)