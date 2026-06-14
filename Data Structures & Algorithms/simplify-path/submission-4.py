class Solution:
    def simplifyPath(self, path: str) -> str:
        strR = []

        for val in path.split("/"):
            if val ==".." and strR:
                strR.pop()
            elif val !="" and val != "." and val != "..":
                strR.append(val)
        if len(strR) == 0:
            return "/" 
        
        return "/" + "/".join(strR)
        
        



'''

thought process: 

cur = [] 

path = "/neetcode/practice//...///../courses"

cur = [/]
str+=/neetcode
cur = []
cur = [/]
str+=/practice
cur = []
if str[i+1] == str[i]:
    continue 
cur = [/]
str+=/courses 

return str
'''