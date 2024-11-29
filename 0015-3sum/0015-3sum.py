class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<1:
            return []
        nums.sort()
        hashset=set()
        n=len(nums)
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            left=i+1
            right=n-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                if current_sum==0:
                    hashset.add(tuple((nums[i], nums[left], nums[right])))
                    left+=1
                    right-=1

                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif current_sum<0:
                    left+=1
                else:
                    right-=1
        return list(hashset)
























        # #Reemeber index should be unique and the triplet but not the element

        # # Iterate through the array to form valid triplets with distinct values

        # for i in range(n):               # Loop from 0 to n

        #     for j in range(i + 1, n):    # loop from i+1 to n


        #         for k in range(j + 1, n):  # loop from j+1 to n

        #             # Ensure the values are distinct before adding and sum to zero
        #             if nums[i]+nums[j]+nums[k]==0:

        #                 current_sum=[nums[i],nums[j],nums[k]] #store the number founds in variable

        #                 current_sum.sort()                    # sort the variable? why? because when the next iteration comes. we will sort and convert it tuple and when it is inserted in the set, it will remove duplicate triplet

        #                 triplet_set.add(tuple((current_sum))) # convert it into tuple


        # # Convert set of triplets to a list of lists

        # return [list(triplet) for triplet in triplet_set]
            

        #     # Time complexity : On(n^3) * log(no. of unique triplet)
        #     # Sc = 2*O(no. of triplets)

        #Reemeber index should be unique and the triplet but not the element
          

        #   """
        #   Approach 2:

        #    # Time complexity : On(n^2) * log(no. of unique triplet)
        #     # Sc = 2*O(no. of triplets)
        #   """
        # triplet_set=set()
        # n=len(nums)
        # # Iterate through the array to form valid triplets with distinct values

        # for i in range(n):               # Loop from 0 to n
        #     hashset=set()
        #     for j in range(i + 1, n):    # loop from i+1 to n
        #         third=-(nums[i]+nums[j])

        #         if third in hashset:


        #             current_sum=[nums[i],nums[j],third] 

        #             current_sum.sort()                  
        #             triplet_set.add(tuple((current_sum))) 
                
        #         hashset.add(nums[j])


        # # Convert set of triplets to a list of lists

        # return [list(triplet) for triplet in triplet_set]





       
        #   """
        #   Approach 2: 2 pointer (optimal solution)

        #    # Time complexity : n log n to sort the array + O(n *n) (n=its for for loop) (n=its for while loop)
        #     # Sc = O(n) (no. of triplets)
        #   """

        # triplet_set = set()  # To store unique triplets
        # nums.sort()  # Sort the array to facilitate the two-pointer technique
        # n = len(nums)

        # for i in range(n):
        #     # Skip duplicate values for the fixed element
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
            
        #     left, right = i + 1, n - 1  # Initialize two pointers
        #     while left < right:
        #         current_sum = nums[i] + nums[left] + nums[right]
        #         if current_sum == 0:
        #             # Found a valid triplet
        #             triplet_set.add((nums[i], nums[left], nums[right]))
        #             left += 1
        #             right -= 1
                    
        #             # Skip duplicates for the second element
        #             while left < right and nums[left] == nums[left - 1]:
        #                 left += 1
                    
        #             # Skip duplicates for the third element
        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1

        #         elif current_sum < 0:
        #             left += 1  # Move left pointer to the right to increase sum
        #         else:
        #             right -= 1  # Move right pointer to the left to decrease sum

        # return [list(triplet) for triplet in triplet_set] 
            

            