class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        res = []

        def dfs(openB, closeB):
            if len(stack) == 2*n:
                res.append("".join(stack))
                return


            # we always start with ( as starting with ) will not be a valid parantheses
            if openB < n:
                stack.append("(")
                dfs(openB+1,closeB)
                stack.pop()

            #there should be enough ( so that if we put closeB it wuld be valid
            if closeB < n and closeB < openB:
                stack.append(")")
                dfs(openB, closeB+1)
                stack.pop()

        dfs(0,0)
        return res