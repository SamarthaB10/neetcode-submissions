class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}

        for word in strs: 

            x = "".join(sorted(word))

            if x in mp: 
                mp[x].append(word)
            
            else:
                mp[x] = [word]
        

        

        res = [] 

        for v in mp: 
            res.append(mp[v])
        return res












'''
{
act : [act,cat]
pots: [pots,tops]

}


'''