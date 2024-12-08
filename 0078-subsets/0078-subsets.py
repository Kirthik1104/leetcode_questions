class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        Number of Subsets:

For an array of length n, there are 2\U0001d45b subsets (including the empty subset and the full set). This is because each element has two choices: to be included or excluded.

        Tc: O(n⋅2^n)
        Sc: O(n.2^n)
        """
        result=[]

        subset=[]

        def dfs(i):
            if i>=len(nums):                  # Base case whrn the index reaches the len(nums) or > len(nums)
                result.append(subset.copy())  # Add the copy of the subset found in the result
                return                        # return after appending the copy of subset to result
            

            # step 2: Decision to add the current number to subset and traverse the next number to add to subset
            subset.append(nums[i])
            dfs(i+1)


            
            """
            Before pop: [1,2]
            Index 0 and Index 1

            After pop: remove current element of current index [2] and index 1 and start from next index 3 : [1, 3]
            Index 0 and Index 2
            """
            # Step 3: Decision to remove the or not consider current number and start from the next index of current index
            subset.pop()
            dfs(i+1)
        
        dfs(0)   # step1: Call the dfs with the starting index
        return result



        