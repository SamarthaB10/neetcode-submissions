class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPali(s:str): 
            if s == s[::-1]: 
                return True 
            else:
                return False 
            
        res =[] 
        subs = []
        def backtrack(i): 

            if i == len(s): 
                res.append(subs.copy())
                return 

            for j in range(i,len(s)): 
                x = s[i : j+1]
                #pick singular character, backtrack 
                if isPali(x): 
                    subs.append(x)
                    backtrack(j+1)
                    subs.pop() 
                
               
        
        backtrack(0)

        return res
                






'''
subs [] 



'''


        






