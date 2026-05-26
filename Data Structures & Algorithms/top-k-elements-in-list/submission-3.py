from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies using a dictionary
        store = {}
        for n in nums: 
            store[n] = store.get(n, 0) + 1
            
        # 2. Initialize our frequency buckets (Index = Frequency count)
        freq = [[] for i in range(len(nums) + 1)] 
        
        # FIXED: Changed variable name to 'num' so it doesn't break 'k'
        # FIXED: Used .append() to store multiple numbers with the same frequency
        for num, v in store.items(): 
            freq[v].append(num)
            
        # 3. Gather results iterating backwards from highest frequency bucket
        res = []
        for i in range(len(freq) - 1, 0, -1): 
            for n in freq[i]: 
                res.append(n)
                if len(res) == k: 
                    return res
'''
{1:1,2:2,3:3} k = 2

nums = [1,2,2,3,10,10]
store
{
    0
    1: []
    2: []
    3: []
}
 

'''
        

