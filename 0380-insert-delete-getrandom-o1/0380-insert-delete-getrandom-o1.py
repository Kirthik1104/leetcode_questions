# https://chatgpt.com/share/675bd184-d834-800b-a4ab-8a08cd46f310

import random
class RandomizedSet:
    """
    # 1) insert : -- insert val if not present and return true for not present
#                 if set already has val--> return false

# 2) removes:---removes val if present in set and return true
#             if set does not have any val return false

# 3) get random: returns a random elememy from set. atleast 1 element is guranteed to be present
    """

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

        mylist[1]=lastelement [1,3,3]--> at position 1 we inserted the value present at the last..now remove last
        mylist.pop()--> [1,3]

        hashmap[lastelement]=index_to_remove--> since val is removed and last position is changed, will update in hashmap. index_to_remove has ind of ele removedso at 
        at that position we will add 2, updating the same in hashmap
        hashmap[3]=0  {1:0, 3:1, 2:1}

        hashmap.pop(val)-->vals is 2-->removes the key and value(index) from hashap since val is also removed from mylist.

        mylits[1,3]
        hashmap={1:0,3:1}


        Swapping---> Wsapping of element whihc is done in O(1)
        ---------
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


"""
Edge case: 
1) Calling random when list and hashmap is empty
-----------------------------------------------
        a) random choice only works if there's element present in"getRandom assumes at least one element exists in the set. If both the list and hashmap are empty, the method will throw an exception because random.choice cannot pick from an empty list.


        b)Handling the Case:

        "To prevent this, we can either:

        Ensure that getRandom is only called when the set is not empty by adding a check.
        Raise a custom error or return a specific value if the list is empty."

        c) 
        def getRandom(self) -> int:
            if not self.mylist:  # Check if the list is empty
                raise ValueError("Cannot get a random element from an empty set")
            return random.choice(self.mylist)

2) Inserting a Duplicate Value----> Alreeady Hnadled by map above

"""


