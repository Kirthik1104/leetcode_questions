import random
class RandomizedSet:

    def __init__(self):
        self.mylist=[]
        self.hashmap={}
    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        
        self.hashmap[val]=len(self.mylist)  # For 1st val, self.mylist list is empty so index value would be 0, 2nd time value will be inserted after this statement so for next element length of new list be 1 which would be the index of the second element
        self.mylist.append(val)
        return True

        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap:
            return False
        
        lastelement=self.mylist[-1]           # To get the last elemnt of the list
        index_to_remove=self.hashmap[val]      # To get the index of the val to be removed

        self.mylist[index_to_remove]=lastelement
        self.hashmap[lastelement]=index_to_remove

        self.mylist.pop()
        self.hashmap.pop(val)
        return True
    def getRandom(self) -> int:
        return random.choice(self.mylist)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# 1) insert : -- insert val if not present and return true for not present
#                 if set already has val--> return false

# 2) removes:---removes val if present in set and return true
#             if set does not have any val return false

# 3) get random: returns a random elememy from set. atleast 1 element is guranteed to be present