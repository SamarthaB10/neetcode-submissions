class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [] 
        pair = sorted(list(zip(position,speed)),reverse = True)

        for st,sp in pair: 
            times.append((target - st) / sp)

            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()
        return len(times)



'''
[(4,2),(1,2),(0,1),(7,1)]
[(0,1)]
times = [] 
1: 
    time = (10-0) /2  = 5 
    times.append(5)
times = 5
2: 
    time = (10-1) / 1 = 9
    if time > times[-1] or not times: 





'''