class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adjList = defaultdict(list)
        visit = set()

        for n1,n2 in prerequisites:
            adjList[n2].append(n1)
        

        #we need to find a cycyle in a directed graph
        #if cycle - False
        def cycle(i):

            if i in visit:
                return True

            if adjList[i] == []:
                return False

            visit.add(i)
            for num in adjList[i]:
                if cycle(num):
                    return True
            visit.remove(i)
            adjList[i] = [] #avoid again going to same nodes again to check
            return False
        

        for i in range(numCourses):
            if cycle(i):
                return False

        return True