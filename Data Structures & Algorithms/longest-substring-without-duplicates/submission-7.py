class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        l = 0 
        maxL = 0 
        seen = set()
        for r in range(len(s)): 
            
           
            while s[r] in seen and l < r: 
                seen.remove(s[l])
                l+=1
                
                
            
            seen.add(s[r])
            maxL = max(maxL,len(seen))

        return maxL
        







'''

s = zxyzxyz

seen = (z,x,y,z)


'''