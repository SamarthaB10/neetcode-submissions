class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        subs = []
        count = {} 
        for num in nums: 
            count[num] = count.get(num,0) + 1
        
       
        def dfs():

            if len(subs) == len(nums): 
                res.append(subs.copy()) 
                return 
            

            for num in count: 
                if count[num] > 0: 
                    subs.append(num)
                    count[num]-=1
                    dfs()

                    subs.pop()
                    count[num]+=1

        dfs()
        return res

