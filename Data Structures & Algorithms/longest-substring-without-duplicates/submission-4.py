class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        store = []
        for char in s: 
            while char in store: 
                store.pop(0)
            
            store.append(char)
            maxLen = max(maxLen,len(store))
        return maxLen

