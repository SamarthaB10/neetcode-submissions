class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0] * len(t)
        stack = [] #[temp,idx]

        for i,x in enumerate(t): 
            while stack and x > stack[-1][0]: 
                sT,sI = stack.pop()
                res[sI] = (i-sI)

            stack.append([x,i])

        return res
'''
0 30
1 38 
2 30 
3 36
4 35
5 40 
6 28 



'''