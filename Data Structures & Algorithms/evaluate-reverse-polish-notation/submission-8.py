class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for val in tokens: 
            if val == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif val == "*":
                z = stack.pop()
                x = stack.pop()
                stack.append(z * x) 
            elif val == "-":
                y = stack.pop()
                x = stack.pop()
                stack.append(x-y) 
            elif val == "/": 
                y = stack.pop()
                x = stack.pop()
                stack.append(int(x/y)) 
            else:
                stack.append(int(val))

        return stack[-1] 

'''
tokens = ["1","2","+","3","*","4","-"]

stack = [1,2]
val = "+" 
stack = [3]
val = "*"
'''