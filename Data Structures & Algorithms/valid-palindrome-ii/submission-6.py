class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = (0,len(s)-1)

        c = 1

        while l <= r and c >0:

            if s[r] == s[l]:
                r-=1
                l+=1
            
            else :
                skipLeft = s[l+1:r+1]
                skipRight = s[l:r]

                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
        return True 


'''
abca
l,r

l = a 
r = abbbca
aa
bc -> b[b] b[c]
'''