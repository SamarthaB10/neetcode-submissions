class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2): 
            newstr +=word1[i]
            newstr +=word2[j]

            i+=1
            j+=1
        
        if j < len(word2): 
            newstr += word2[j:]
        else:
            newstr+=word1[i:]
        

        return newstr
    

'''
abc xyzzc

i j 

ax
by
cz



'''