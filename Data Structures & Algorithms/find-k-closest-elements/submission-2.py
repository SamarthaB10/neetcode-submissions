import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        
        vals = []
        for v in arr:
            dis = abs(v-x)
            vals.append((dis,v))
        
        heapq.heapify(vals)

        vals = sorted(vals)
        res = [] 
        for i in range(k): 
            res.append(vals[i][1])
        return sorted(res)


'''

arr = [2,4,5,8]
dict = {
2:4
4:2
5:1
8:3

}

'''