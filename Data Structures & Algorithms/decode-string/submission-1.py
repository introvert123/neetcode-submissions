class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        for ch in s:
            if ch == ']':
                string = ""
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop() #remove [

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * string)
 
            else:
                stack.append(ch)

        return "".join(stack)