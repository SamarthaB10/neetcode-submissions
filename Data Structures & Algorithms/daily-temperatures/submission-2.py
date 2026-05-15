class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]*(len(t))

        for i in range(len(t)): 
            j = i+1

            while(j < len(t)): 
                if(t[j] > t[i]): 
                    res[i] = j-i
                    break 
                else:
                    j+=1
        return res


        