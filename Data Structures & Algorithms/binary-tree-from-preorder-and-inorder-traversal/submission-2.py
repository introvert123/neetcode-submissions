# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        #most optimized solution compared to original
        map = {}

        for i in range(len(inorder)):
            map[inorder[i]] = i
        
        self.pre_idx = 0


        def dfs(l,r):

            if l <= r:
                root = TreeNode(preorder[self.pre_idx])
                
                #find the index where this elemnt of preorder lies in inorder
                mid = map[preorder[self.pre_idx]]
                self.pre_idx += 1

                root.left = dfs(l,mid-1)
                root.right = dfs(mid+1,r)
                return root
            else:
                return None

        
        return dfs(0,len(inorder) - 1)
