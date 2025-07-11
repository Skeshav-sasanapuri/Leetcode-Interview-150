import random

class RandomizedSet:

    def __init__(self):
        self.values_list = []
        self.index_dict = {}
        self.curr_last_index =  0

    def insert(self, val: int) -> bool:
        if val not in self.index_dict:
            self.values_list.append(val)
            self.index_dict[val] = self.curr_last_index
            self.curr_last_index += 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index_dict:
            update_dict_key = self.values_list[self.curr_last_index-1]
            update_dict_val = self.index_dict[val]
            self.values_list[self.curr_last_index-1], self.values_list[self.index_dict[val]] = self.values_list[self.index_dict[val]], self.values_list[self.curr_last_index-1] 
            self.index_dict[update_dict_key] = update_dict_val
            self.values_list.pop()
            self.index_dict.pop(val)
            self.curr_last_index -= 1
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand_index = random.randint(0, self.curr_last_index-1)
        return self.values_list[rand_index]        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()