class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen ={}
        need = {} 
        for char in s1:
            need[char] = need.get(char,0) + 1 
        l = 0 
        for r in range(len(s2)):
            seen[s2[r]] = seen.get(s2[r],0) +  1
            if (r-l + 1) == len(s1): 
                if seen == need: 
                    return True
                
                seen[s2[l]] -= 1
                if seen[s2[l]] == 0: 
                    del seen[s2[l]]
                l+=1

        return False 
        

                
'''
lecabee 
{
l: 1
e : 3
c: 1
a: 1
b : 1

}


'''