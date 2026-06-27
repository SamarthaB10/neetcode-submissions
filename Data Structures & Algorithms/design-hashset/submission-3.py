class MyHashSet:

    def __init__(self):
        self.Hs = []

    def add(self, key: int) -> None:
        if key not in self.Hs:
            self.Hs.append(key)

    def remove(self, key: int) -> None:
        try:
            val = self.Hs.index(key)
            del self.Hs[val]
        except Exception as e:
            return
        
        

    def contains(self, key: int) -> bool:
        return key in self.Hs

            


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)