class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}

        for index, num in enumerate(nums):
            diff = target - num 
          
            if diff in hashmap:
                return hashmap[diff], index
            else:
                hashmap[num]=index
              



























#         """
#         Suumary
#         --------
#         Absolutely! To solve this problem, I used a hash map to store numbers and their indices as I iterate through the array. For each number, I calculate its complement (what’s needed to reach the target) and check if it’s already in the hash map. If it is, I return the indices.This approach ensures that I solve the problem in O(n) time with O(n) space, which is efficient and meets the problem constraints."
#         """
#         # Dictionary to store numbers and their indices
#         hashmap={}

#         # Iterate through the array
#         for i, num in enumerate(nums):

#             # Calculate the complement: target - num
#             diff=target-num

#             # if diff exits in the hashmap
#             if diff in hashmap:
#                 return [hashmap[diff], i]  # return the index of the diff and the current index

#             # else iff  diff not in hashmap, store the current number with its index in the hash map
#             hashmap[num]=i



#             """
#             Edge Case:
#             ----------

#             1) Negative no: 
#             Input: nums = [-3, 4, 7, 1], target = 1
#             The solution handles negative numbers well because the complement is calculated as target - num, which works for both positive and negative numbers 
#             For instance:
#             Complement for -3 is 1−(−3)=4.

#             2) Single element: Description saya there exits 1 solution
#             Can still use checkL if len(list)<2---> Need two elements to compare

#             3) Handles Duplicates: if same numbers present and one of the duplicates  + any random is used to get the tarhet. which duplicate index to use?
#             Key Takeaway: The last occurrence of the complement is used if duplicates exist.

#             """
       
# # Code Walkthrough Using Test Case nums2 = [3, 4, 6, 2, 10], target2 = 8:

# # Step 0:
# # --------
# # Current number: 3
# # Complement: 8 - 3 = 5
# # Check: Is 5 in the hash map? No
# # Add 3 to the hash map: {3: 0}

# # Step 1:
# # -------
# # Current number: 4
# # Complement: 8 - 4 = 4
# # Check: Is 4 in the hash map? No
# # Add 4 to the hash map: {3: 0, 4: 1}

# # Step 2:
# # -------
# # Current number: 6
# # Complement: 8 - 6 = 2
# # Check: Is 2 in the hash map? No
# # Add 6 to the hash map: {3: 0, 4: 1, 6: 2}

# # Step 3:
# # -------
# # Current number: 2
# # Complement: 8 - 2 = 6
# # Check: Is 6 in the hash map? Yes, at index 2
# # Return: [2, 3]
        