class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        

        
        counter = 0
        sumI = 0

        l = 0 

        for r in range(len(arr)): 
            sumI += arr[r]

            if r-l +1 == k: 
                avg = sumI // k
                if avg >= threshold:
                    counter +=1

                sumI -= arr[l]
                l+=1
            
                
            
        return counter


