class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {} #key is key, val is Node with key and val
        self.capacity = capacity
        # dummy left and right nodes where left is LRU and right is MRU
        self.left = Node(0,0) 
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node) -> None:
        # removing any node
        nxt = node.next
        prv = node.prev
        prv.next = nxt
        nxt.prev = prv

    
    def insert(self, node: Node) -> None:
        # inserting at right
        prv = self.right.prev
        # left connect
        prv.next = node
        node.prev = prv
        #right connect
        node.next = self.right
        self.right.prev = node

        
    def get(self, key: int) -> int:
        # whenever we do get, it becomes the most recently used so it has 
        # to be removed and inserted at the right
        if key in self.hashmap:
            self.remove(self.hashmap[key])
            self.insert(self.hashmap[key])
            return self.hashmap[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            #remove the node from DLL
            self.remove(self.hashmap[key])
        # first insert into hashmap and also doubly linked list to keep track of LRU
        # why we are inserting everytime is bcoz we have to, and remove LRU instead
        self.hashmap[key] = Node(key,value)
        self.insert(self.hashmap[key])
        
        if self.capacity < len(self.hashmap):
            # remove LRU and lRU is always next to left node
            del self.hashmap[self.left.next.key]
            self.remove(self.left.next)
        

        
