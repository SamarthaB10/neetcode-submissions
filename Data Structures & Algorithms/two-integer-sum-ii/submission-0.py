class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        store ={} 

        for i in range(len(nums)): 
            dif = target - nums[i]

            if dif in store: 
                return[store[dif],i+1]
            
            store[nums[i]] = i+1