from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
             return False 
        x = Counter(s)
        y = Counter(t) 

        for l in s: 
            if(x[l] != y[l]): 
                return False 
        return True 