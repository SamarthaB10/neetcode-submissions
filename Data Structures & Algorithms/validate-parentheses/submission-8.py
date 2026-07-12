class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        mapI = {
            ")" : "(", 
            "}" : "{", 
            "]" : "["
        }

        for char in s: 
            if char in mapI:
                if stack and stack[-1] == mapI[char]: 
                    stack.pop() 
                else:
                    return False 
            else:
                stack.append(char)

            
        return len(stack) == 0 
            

           


'''
 [ { ]

'''