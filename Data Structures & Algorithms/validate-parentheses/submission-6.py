class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapI = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }

        for char in s: 
            if char not in mapI: 
                stack.append(char)
            else:
                if stack and stack[-1] == mapI[char]: 
                    stack.pop() 
                else:
                    return False 

            
        return len(stack) == 0 
            

           


'''
 [ { ]

'''