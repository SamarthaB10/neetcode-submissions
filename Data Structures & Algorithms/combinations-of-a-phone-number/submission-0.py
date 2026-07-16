class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    
        mal = {
            "2":"abc",
            "3":"def","4": "ghi","5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv",'9':"wxyz"
        }   

        res =[] 
        subs = []

        if not digits: 
            return []


        def dfs(i): 
            if i == len(digits): 
                res.append("".join(subs.copy()))
                return 
            
            chars = mal[digits[i]]

            for char in chars: 
                subs.append(char)
                dfs(i+1)

                subs.pop() 
               
        
        dfs(0)
        return res 


