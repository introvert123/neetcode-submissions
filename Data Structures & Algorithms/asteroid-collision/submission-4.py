class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for i in range(len(asteroids)):
            alive = True
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
                    alive = False
                    break
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()
                else:
                    # when we don't want to add the element to stack
                    alive = False
                    break

            if alive:
                stack.append(asteroids[i])
                
        return stack

        