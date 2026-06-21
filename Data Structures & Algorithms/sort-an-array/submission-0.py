class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr1,arr2) -> List[int]:
            res = []
            i,j = (0,0)

            while i < len(arr1) and j < len(arr2): 
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i+=1
                
                else:
                    res.append(arr2[j])
                    j+=1
                
            res.extend(arr1[i:])
            res.extend(arr2[j:])
            return res 
        
        def mergeSort(nums):

            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2

            leftH = nums[:mid]
            rightH = nums[mid:] 

            left = mergeSort(leftH)
            right = mergeSort(rightH)

            return merge(left,right)
        
        return mergeSort(nums)

