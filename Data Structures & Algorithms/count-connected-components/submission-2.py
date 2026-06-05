class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = defaultdict(list)
        visited = set()
        count = 0

        for i in range(len(edges)):
            adjList[edges[i][0]].append(edges[i][1])
            adjList[edges[i][1]].append(edges[i][0])

        def dfs(i):
            
            visited.add(i)
            for val in adjList[i]:
                if val not in visited:
                    dfs(val)


        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count

        