class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        minVal = self.stack[-1]
        stack2 = []
        while len(self.stack) != 0:
            if (self.stack[-1] < minVal):
                minVal = self.stack[-1]
            stack2.append(self.stack[-1])
            self.stack.pop()

        while len(stack2) != 0:
            self.stack.append(stack2[-1])
            stack2.pop()
        return minVal
        
