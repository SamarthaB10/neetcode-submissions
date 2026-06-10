class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m,ma = (1,max(piles))
        minSpeed = ma
        while m <= ma:
            mi = (m + ma) // 2
            total_hrs = 0

            for pile in piles:
                total_hrs+= math.ceil(pile/mi)
            
            if total_hrs <= h:
                minSpeed = min(minSpeed,mi)
                ma = mi -1
                
            
    
            else:
                m = mi + 1
               
        return minSpeed




            


        







'''
objective: find the min eating speed to finish all without 
eating rate = 1

piles = [1,4,3,2]


for i range(len(piles)): 
    


'''