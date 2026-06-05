class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPos = sorted(zip(position,speed),reverse= True)

        res = [] 

        for nums in sortedPos: 
            pos,sp = nums
            time = (target - pos) / (sp)

            
            if not res or res[-1] < time: 
                res.append(time)
        
        return len(res)

'''

'''

