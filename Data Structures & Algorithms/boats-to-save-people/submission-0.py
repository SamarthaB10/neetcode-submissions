class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int: 
        res = [] 
        people.sort() 
        l = 0

        r=len(people) -1


        while l <= r: 
            num = people[l] + people[r]

            if num > limit:
                res.append([people[r]])
                r-=1
            
            else:
                res.append([people[r],people[l]])
                l+=1
                r-=1
        
        
        return len(res)
            

'''
1,2,2,3,3
[3]
[3]
[1,2]
'''
        
              






















'''
1,2,4,5



'''