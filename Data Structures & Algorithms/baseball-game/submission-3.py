class Solution:
    def calPoints(self, operations: List[str]) -> int:
        store = [] 
        sumS = 0 
        for x in operations:
            if x == "+": 
                new = store[-1] + store[-2]
                sumS +=new
                store.append(new)

                    
            elif x == "D": 
                new = store[-1] * 2
                sumS +=new
                store.append(new)

            elif x == "C": 
                y = store.pop()
                sumS -=y
            
            else: 
                x = int(x)
                store.append(x)
                sumS +=x


        return sumS




'''
ops = ["1","2","+","C","5","D"]
store = [] 
for w in ops


'''