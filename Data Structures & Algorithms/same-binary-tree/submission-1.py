# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #trying BFS approach

        if p == None and q == None:
            return True
        

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 != None and node2 != None and node1.val != node2.val:
                return False
            elif node1 == None and node2 != None or node1 != None and node2 == None:
                return False

            if node1:
                q1.append(node1.left)
                q1.append(node1.right)
            if node2:
                q2.append(node2.left)
                q2.append(node2.right)
        
        if len(q1) == 0 and len(q2) == 0:
            return True
        else:
            return False

