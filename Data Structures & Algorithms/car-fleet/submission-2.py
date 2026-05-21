class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = sorted(list(zip(position,speed)),reverse = True)
        times =[] 
        for pos,sp in x: 

            time = (target - pos) / sp
            if not times or time > times[-1]: 
                times.append(time)
        
        return len(times)






'''

10

[4,1,0,7][2,2,1,1]  t = 10
distance []


'''