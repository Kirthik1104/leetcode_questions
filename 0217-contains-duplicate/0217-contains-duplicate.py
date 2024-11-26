class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Using Hashmap
        1) 1 for loop to map values with no. of occurence
        2) 2nd for loop to acces the value whose occurece is greate than 2
        """
        hashmap={}
        for num in nums:
            if num in hashmap:
                hashmap[num]+=1
            else:
                hashmap[num]=1
        print(hashmap)
        for val in hashmap.values():
            if val>1:
                return True
        return False


        """
        Using Hashset
        1) Using 1 for loop to add unique values to hashset and if same values repeat return true immediately
        2) If same values not present till the end, return false at the end of loop
        """
        hashset=set()
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

### Time and Space Complexity

#### HashMap Approach:
- **Time Complexity**: `O(n)`  
  - `O(n)` to build the hashmap + `O(k)` to iterate over values (`k <= n`).
- **Space Complexity**: `O(n)`  
  - Stores counts for up to `n` unique elements.

#### HashSet Approach:
- **Time Complexity**: `O(n)`  
  - `O(n)` for checking membership and adding elements.
- **Space Complexity**: `O(n)`  
  - Stores up to `n` unique elements.

---

### Summary
- Both approaches have **O(n)** time and space complexity.  
- **HashSet** is simpler and avoids an extra loop, making it slightly faster in practice.
