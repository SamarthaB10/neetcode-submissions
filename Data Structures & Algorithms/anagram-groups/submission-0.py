class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for word in strs : 
            x = sorted(word)
            y =''.join(x)
            if y in store:
                store[y].append(word)
            else: store[y] = [word]
        return list(store.values())



'''
Thinking: 
Probably go with hashing 

{act:}



'''