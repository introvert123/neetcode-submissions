class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        list1 = []
        for i in range(n):
            if tokens[i] in "+-*/" and list1:
                if tokens[i] == '+':
                    list1.append(list1.pop() + list1.pop())
                elif tokens[i] == '*':
                    list1.append(list1.pop() * list1.pop())
                elif tokens[i] == '/':
                    num = list1.pop()
                    list1.append(int(list1.pop() / num))
                elif tokens[i] == '-':
                    num = list1.pop()
                    list1.append(list1.pop() - num)

            else:
                list1.append(int(tokens[i]))

        return list1[-1]      