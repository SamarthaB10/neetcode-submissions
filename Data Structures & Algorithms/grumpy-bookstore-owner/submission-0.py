class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    
    
        l = 0 
        countO = 0
        for i in range(len(customers)):

            if grumpy[i] == 0:
                countO +=customers[i]    
        extra = 0
        max_extra = 0
        for r in range(len(grumpy)):

            if grumpy[r] == 1:
                extra +=customers[r]

            window = r-l +1

            if window == minutes:
                max_extra = max(max_extra,extra)
                if grumpy[l] ==1:
                    extra -= customers[l]
                
                l+=1
        

        return countO +max_extra
            
                  

                

        

'''
1+1+2+1+1+7+5 = 18
grumly = [0,1,0,1,0,1,0,1]



'''