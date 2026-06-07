class Solution:
    def mySqrt(self, x: int) -> int:
        tg = 0 
        for i in range(x+1): 
            if i*i > x:
                break
            
            tg = i
            
        return tg
        
        

'''
l * l 



'''

