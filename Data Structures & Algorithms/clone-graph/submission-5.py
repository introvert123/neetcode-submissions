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

        #has old nodes
        queue = deque()
        queue.append(node)

        #to store value and their newNode so that I can use it to connect neighbors
        map1 = {}
        map1[node.val] = Node(node.val)

        while queue:
            temp = queue.popleft()
            for neighbor in temp.neighbors:
                if neighbor.val not in map1:
                    temp1 = Node(neighbor.val) #create new node
                    map1[neighbor.val] = temp1 #save in map
                    queue.append(neighbor)

                map1[temp.val].neighbors.append(map1[neighbor.val]) #adding neighbors
                
        return map1[node.val]
        