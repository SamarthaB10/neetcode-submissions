class MyHashMap:

    def __init__(self):
        self.Hs= {}

    def put(self, key: int, value: int) -> None:
        
            self.Hs[key] = value
    

    def get(self, key: int) -> int:
        if key in self.Hs:
            return self.Hs[key]
        else:
            return -1 

    def remove(self, key: int) -> None:
        try:
            del self.Hs[key]
        except Exception as e:
            return 

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)