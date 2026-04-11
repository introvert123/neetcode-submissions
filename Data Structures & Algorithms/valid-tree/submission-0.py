class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n == 0:
            return True

        adjMap = defaultdict(list)
        visited = set()

        for n1,n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        def dfs(val, prev):

            if val not in visited:
                visited.add(val)
            else: #val in visited meaning there's a loop
                return False

            for node in adjMap[val]:                                                                             
                if node != prev:
                    if dfs(node, val) == False: #there's a loop - ret False immeditaley
                        return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n

        
        