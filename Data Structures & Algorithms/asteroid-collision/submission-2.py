class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for val in asteroids:
            if not stack: 
                stack.append(val)
                continue 
            alive = True
            while alive and stack and stack[-1] > 0 and val < 0:
                if abs(val) > stack[-1]: 
                    stack.pop()
                elif abs(val) == abs(stack[-1]):
                    stack.pop()
                    alive = False 
                else:
                    alive = False
            if alive:
                stack.append(val)
        return stack
