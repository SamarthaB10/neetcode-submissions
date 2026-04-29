from collections import deque 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {} 
        for num in nums: 
            store[num] = store.get(num,0) + 1
        
        sortedstore = list(dict(sorted(store.items(), key = lambda k: k[1], reverse = True )).keys())

        return sortedstore[:k]

