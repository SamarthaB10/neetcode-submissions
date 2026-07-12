class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = [] 
        subs = []

        rem = {"(" : n,
               ")" : n}
        def dfs():

            if len(subs) == (2*n):
                res.append("".join(subs.copy()))
                return 
            
            if rem["("] > 0: 
                subs.append("(")
                rem["("] -=1
                dfs()
                subs.pop()
                rem["("] +=1
            if rem["("] < rem[")"] and rem[")"] > 0: 
                subs.append(")")
                rem[")"] -=1

                dfs()
                subs.pop()
                rem[")"] +=1

            
        
        dfs()
        return res




'''




'''
