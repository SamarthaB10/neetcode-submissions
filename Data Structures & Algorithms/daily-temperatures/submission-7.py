class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = [] #(v,i) 
        indic = [0] * len(temp)
        for i,v in enumerate(temp):
            while stack and v > stack[-1][0]: 
                st,si = stack.pop() 
                indic[si] = i-si 
            
            stack.append([v,i])
        

        return indic
