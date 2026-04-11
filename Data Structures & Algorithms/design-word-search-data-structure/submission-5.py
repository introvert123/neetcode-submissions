class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False 


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            idx = ord(c) - ord('a')
            
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]
        
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        # we need to do dfs as there could be multiple branches and not the first one will result in word

        def dfs(curr, i):
            if i == len(word):
                return curr.isLeaf

            c = word[i]

            if c == '.':
                for child in curr.children:
                    if child and dfs(child, i+1):
                        return True
                return False
            else:
                idx = ord(c) - ord('a')
                if curr.children[idx] == None:
                    return False
                return dfs(curr.children[idx], i+1)

        return dfs(self.root, 0) 

        

