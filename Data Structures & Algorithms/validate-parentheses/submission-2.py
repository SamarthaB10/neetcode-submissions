class Solution:
    def isValid(self, s: str) -> bool:
        if not s: 
            return False 
        store = {'(': ')', '{': '}', '[':']'}
        temp = [] 
        for l in s : 
            if l in store: 
                temp.append(l)
            else: 
                if not temp: 
                    return False
                y = temp.pop() 
                if store[y] ==l:
                    continue 
                else: 
                    return False 
        
        return len(temp) ==0
'''
()



temp = [  (  { }


'''        