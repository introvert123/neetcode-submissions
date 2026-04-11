class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if curr.children[idx] == None:
                node = TrieNode()
                curr.children[idx] = node
            else:
                node = curr.children[idx]
            
            curr = node
        
        curr.isLeaf = True
        
    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')

            if curr.children[idx] == None:
                return False
            
            curr = curr.children[idx]
        
        return curr.isLeaf

        

    def startsWith(self, prefix: str) -> bool:

        curr = self.root

        for c in prefix:
            idx = ord(c) - ord('a')

            if curr.children[idx] == None:
                return False
            
            curr = curr.children[idx]
        
        return True
        
        