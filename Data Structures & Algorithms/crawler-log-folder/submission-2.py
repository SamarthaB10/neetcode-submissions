class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        store = []

        for log in logs: 
           

            if log == "./": 
                continue 
            
            if log == "../" and store: 
                store.pop()
            
            if log != "../":
                store.append(log)

            
        

        return len(store)



'''




'''