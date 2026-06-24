class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        store1 = {}
        for char in s1: 
            store1[char] = store1.get(char,0) + 1
        
        l = 0 
        store2 = {}
        for r in range(len(s2)): 
            store2[s2[r]] = store2.get(s2[r],0) +1
            
        
            while r - l + 1 > window and l < r:
                store2[s2[l]] -=1
                

                if store2[s2[l]] == 0:
                    del store2[s2[l]] 
                
                
                
                l+=1
            if store2 == store1:
                    return True 

         
        
        return False 
            


'''


store2
{


e:1
c:1


}




'''