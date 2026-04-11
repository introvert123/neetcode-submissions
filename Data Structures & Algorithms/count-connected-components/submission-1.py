class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adjList = defaultdict(list)

        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        
        visited = set()

        def dfs(val):

            if val not in visited:
                visited.add(val)
            else:
                return
            
            for node in adjList[val]:
                dfs(node)

            return

        cnt = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                cnt += 1

        return cnt


        #prev like other problem is not reqd is bcoz there are no loops here
        #prev was reqd only bcoz we were detecting the loops



            

        