class Solution:
    def climbStairs(self, n: int) -> int:
        seen = {} 

        def backTrack(num): 
            if num == 1:
                return 1
            if num == 2: 
                return 2


            if num in seen:
                return seen[num]
            
            ans = backTrack(num - 1) + backTrack(num - 2)

            seen[num] = ans
            return ans
        
        return backTrack(n)

        