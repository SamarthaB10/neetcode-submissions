class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [] 
        
        for val in asteroids:
            alive = True  
            while alive and stack and stack[-1] > 0 and val < 0:
                x = stack[-1] + val #[3,5,-6]

                if x == 0: 
                    stack.pop()
                    alive = False 
                elif x < 0 : 
                    stack.pop()
                else: 
                    alive = False 
            if alive:
                stack.append(val)
        
        return stack