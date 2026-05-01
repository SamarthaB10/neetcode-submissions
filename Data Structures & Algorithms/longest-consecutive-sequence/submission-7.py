class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums :
            return 0 
        else : x = sorted(set(nums))
        maxS =1 
        curS = 1
        j= 1
        while(j < len(x)): 
            if x[j] == x[j-1] + 1: 
                curS +=1 
            else:
                maxS = max(curS,maxS)
                curS = 1
            j+=1
        return max(maxS,curS)