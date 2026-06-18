class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adjList = defaultdict(list)

        for n1,n2 in prerequisites:
            adjList[n2].append(n1)

        res = []
        visit = set()
        path = set()

        def cycle(i):

            if i in visit:
                return True

            visit.add(i)
            for num in adjList[i]:
                if cycle(num):
                    return True
            
            visit.remove(i)
            if i not in path:
                res.insert(0,i)
                path.add(i)
            adjList[i] = []
            return False


        for i in range(numCourses):
            if cycle(i):
                return []
        
        return res
        