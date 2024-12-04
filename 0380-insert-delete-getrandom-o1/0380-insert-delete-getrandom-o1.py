import random
class RandomizedSet:

    def __init__(self):
        self.mylist=[]
        self.hashmap={}
    def insert(self, val: int) -> bool:
        if val in self.hashmap:  # if val is already present as keys return False
            return False
        
        self.hashmap[val]=len(self.mylist)  # For 1st val, self.mylist list is empty so index value would be 0, value is also appended to mylist, so len of my list is 1. so for next call element length of new list be 1 which would be the index of the second element and so on
        self.mylist.append(val)
        return True

        
    def remove(self, val: int) -> bool:
        if val not in self.hashmap:    # If val is not present as keys in hashmap, nothing to remove. return False
            return False
        
        """
        To remove val=2
        ------------
        mylist=[1,2,3]
        hashmap={1:0, 2:1, 3:2}

        lastelement= mylist[-1] which gives 3
        index_to_remove= hashmap[2] which gives the index of val to removed= 1

        mylist[1]=lastelement [1,3,3]--> at position 2 we inserted the same value as the last..now remove last
        mylist.pop()--> [1,3]

        hashmap[lastelement]=index_to_remove--> since val is removed and last position is changed, will update in hashmap
        hashmap[3]=0  {1:0, 3:1, 2:1}

        hashmap.pop(val)-->vals is 2-->removes the key and value from hashap since val is also removed from mylist

        mylits[1,3]
        hashmap={1:0,3:1}



        """

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