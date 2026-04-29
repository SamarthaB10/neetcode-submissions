from collections import deque 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {} 
        returner = deque() 
        temp = maxV= 0
        for num in nums: 
            store[num] = store.get(num,0) + 1
    
        for num in store.values(): 
            temp = num 
            maxV=max(temp,maxV)
            returner.appendleft(maxV)
        
        sortedstore = list(dict(sorted(store.items(), key = lambda k: k[1], reverse = True )).keys())

        return sortedstore[:k]

