class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for list1 in board:
            s = set()
            for x in list1:
                if x == '.':
                    continue
                elif x not in s:
                    s.add(x)
                else:
                    return False

        n = len(board)
        newList = [[]]
        for i in range(n):
            list2 = []
            for list1 in board:
                list2.append(list1[i])
            newList.append(list2)

        for list1 in newList:
            s = set()
            for x in list1:
                if x == '.':
                    continue
                elif x not in s:
                    s.add(x)
                else:
                    return False

        i = 0
        while i < n:
            if i % 3 == 0:
                dict1 = defaultdict(set)
            j = 0
            k = 0
            while j < n:
                if j !=0 and j % 3 == 0:
                    k = k + 1
                if board[i][j] == '.':
                    j += 1
                    continue
                elif board[i][j] not in dict1[k]:
                    dict1[k].add(board[i][j])
                else:
                    return False
                j += 1
            i += 1

        return True