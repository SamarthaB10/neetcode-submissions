class Solution:
    def merge(self, nums: List[int], m: int, nums1: List[int], n: int) -> None:
        
        i,j = (m-1,n-1)
        k = i +j + 1 
        
        while i >= 0 and j>= 0: 

            if nums[i] > nums1[j]:
                nums[k] = nums[i]
                i-=1
            else:
                nums[k] = nums1[j]
                j-=1
            k-=1
        while j >= 0: 
            nums[k] = nums1[j]
            j-=1
            k-=1







'''
[10,20,20,40,0,0] [1,2]
is 40 > 2?
10,20,20,2,40,0


'''