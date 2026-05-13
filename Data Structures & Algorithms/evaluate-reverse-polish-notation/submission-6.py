class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["*","-","+","/"]
        stack = []  
        for i in tokens:
            if i not in operators: 
                stack.append(int(i))
            else: 
                y = stack.pop()
                z = stack.pop()
                if i == "*": 
                    stack.append(z * y)
                elif i == "+": 
                    stack.append(z+y)
                elif i == "-": 
                    stack.append(z-y)
                else:
                    stack.append(int(z/y))
        return stack[-1]
                

                    
            
                



'''
tokens = ["1","2","+","3","*","4","-"]
stack [1,2,]
+ 
1 + 2 
stack = [1,2,3] 
3 * 3
stack = [9]
4 - 
9 - 4 = 5
return 5

'''