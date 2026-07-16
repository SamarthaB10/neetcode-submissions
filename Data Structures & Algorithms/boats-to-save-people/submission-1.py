class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int: 
        count = 0
        people.sort() 
        l = 0

        r=len(people) -1


        while l <= r: 
            num = people[l] + people[r]

            if num > limit:
                count+=1
                r-=1
            
            else:
                count +=1
                l+=1
                r-=1
        
        
        return count
            

'''
1,2,2,3,3
[3]
[3]
[1,2]
'''
        
              






















'''
1,2,4,5



'''