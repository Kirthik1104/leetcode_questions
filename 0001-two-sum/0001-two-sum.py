class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store numbers and their indices
        hashmap={}

        # Iterate through the array
        for i, num in enumerate(nums):

            # Calculate the complement: target - num
            diff=target-num

            # if diff exits in the hashmap
            if diff in hashmap:
                return [hashmap[diff], i]  # return the index of the diff and the current index

            # else iff  diff not in hashmap, store the current number with its index in the hash map
            hashmap[num]=i
       
# Code Walkthrough Using Test Case nums2 = [3, 4, 6, 2, 10], target2 = 8:

# Step 0:
# --------
# Current number: 3
# Complement: 8 - 3 = 5
# Check: Is 5 in the hash map? No
# Add 3 to the hash map: {3: 0}

# Step 1:
# -------
# Current number: 4
# Complement: 8 - 4 = 4
# Check: Is 4 in the hash map? No
# Add 4 to the hash map: {3: 0, 4: 1}

# Step 2:
# -------
# Current number: 6
# Complement: 8 - 6 = 2
# Check: Is 2 in the hash map? No
# Add 6 to the hash map: {3: 0, 4: 1, 6: 2}

# Step 3:
# -------
# Current number: 2
# Complement: 8 - 2 = 6
# Check: Is 6 in the hash map? Yes, at index 2
# Return: [2, 3]
        