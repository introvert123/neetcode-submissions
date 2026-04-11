"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None

        created = {}
        created[node.val] = Node(node.val)

        queue = deque([node])    

        while queue:
            temp = queue.popleft()

            for neighbor in temp.neighbors:
                if neighbor.val not in created:
                    created[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)

                created[temp.val].neighbors.append(created[neighbor.val])
                    


        return created[node.val]
        
        
        