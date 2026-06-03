class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {} 
        countS ={} 
        for char in t: 
            countT[char] = countT.get(char,0) + 1

        
        l = 0 
        res = [float("inf"),0,0]
        total_needed =sum(countT.values())
        for r in range(len(s)):
            char = s[r]
            countS[char] = countS.get(char,0) +1
            if char in countT and countS[char] <= countT[char]: 
                total_needed -=1
            

            while total_needed == 0: 
                if r-l + 1  < res[0]: 
                    res = [r-l+1,l,r]
                char_left = s[l]
                countS[char_left] -=1

                if char_left in countT and countS[char_left] < countT[char_left]: 
                    total_needed +=1

                l+=1
        length,start,end = res
        return s[start:end+1] if length != float("inf") else ""
        




'''
countT = 
{
"X": 1
"Y" : 1
"Z" : 1
}

totalNeeded = 3
OUXTEYZ
o,u,x,
'''