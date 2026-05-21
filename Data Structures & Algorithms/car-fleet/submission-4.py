class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for p, s in pair:
            time = (target - p) / s
            stack.append((time))
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
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