import random

class RandomizedSet:

    def __init__(self):
        self.s = []

    def insert(self, val: int) -> bool:
        for element in self.s:
            if element == val:
                return False
        self.s.append(val)
        return True

    def remove(self, val: int) -> bool:
        for i in range(len(self.s)):
            if self.s[i] == val:
                self.s.pop(i)
                return True
        return False

    def getRandom(self) -> int:
        index = random.randint(0, len(self.s)-1)
        return self.s[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()