from collections import deque 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = {} 
        for num in nums: 
            store[num] = store.get(num,0) + 1
        
        sorted_store = [k for k, v in sorted(store.items(), key=lambda x: x[1], reverse=True)]
        return sorted_store[:k]

