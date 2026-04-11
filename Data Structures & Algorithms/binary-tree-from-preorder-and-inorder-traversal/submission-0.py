# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # creating a hashmap to store inorder indices and values
        map = {}
        for k in range(len(inorder)):
            map[inorder[k]] = k
        
        #this index is to track preorder list
        self.pre_idx = 0

        def dfs(l,r):

            if l <= r:
                key = preorder[self.pre_idx]
                self.pre_idx += 1
                root = TreeNode(key)
                mid = map[key]
                root.left = dfs(l, mid - 1)
                root.right = dfs(mid + 1, r)
                return root
            else:
                return None

        return dfs(0, len(inorder) - 1)

        


        