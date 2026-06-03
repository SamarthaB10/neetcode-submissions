class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table = {} 
        maxFrq = 0
        maxL = 0
        l= 0 
        for r in range(l,len(s)): 
            char = s[r]
            table[char] = table.get(char,0) +1
            maxFrq = max(maxFrq, table[char])

            windowLen = r-l + 1
            if windowLen - maxFrq > k:
                
                table[s[l]] -=1
                l+=1
            
            maxL = max(maxL,r-l + 1)

        return maxL




'''
X Y Y X     k = 2
AAABABB  k =1 
table = {
"A" : 3            maxFrq = 3
"B" : 1

k = 2
minVa = 3

}




'''