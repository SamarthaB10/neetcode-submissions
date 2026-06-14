class Solution:
    def simplifyPath(self, path: str) -> str:
        x = path.split("/")

        res = []
        for vals in x:
            if res and vals == "..":
                res.pop() 
            
            elif vals != "" and vals != ".." and vals!= ".":
                res.append(vals) 

        if len(res) == 0:
            return "/"
        
        return "/" + "/".join(res)