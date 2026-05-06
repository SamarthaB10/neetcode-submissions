class Solution:
    def isPalindrome(self, s: str) -> bool:
        y = s.lower() 
        f = 0 
        b = len(s) -1 
        x = True 
        while(f<=b and f < len(s) - 1): 
            if not y[f].isalnum():
                f+=1
                continue
            if not y[b].isalnum(): 
                b-=1
                continue
            if y[f] != y[b]:
                x = False 
                return x 
            else:
                f+=1
                b-=1
        return x 