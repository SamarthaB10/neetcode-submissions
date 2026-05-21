class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        x = sorted(list(zip(position,speed)),reverse = True)
        store = [] 
        for st,sp in x:
            time = (target - st)/sp

            if not store or time > store[-1]: 
                store.append(time)

        return len(store)

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