class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n             # List to store the max height from left to right
        right=[0]*n            # List to store the max height from right to left
        res1=0                 # Variable to store the max height of left
        res2=0                 # Variable to store the max height of right

        for i in range(n):     
            res1=max(res1, height[i]) # Traversing and storing the max height encountered from left to right
            left[i]=res1              # Filling max height from left to right

            j=n-i-1                # n-i-1 : To start the index from right to left

            res2=max(res2, height[j])  # Traversing and storing the max height encountered from right to left
            right[j]=res2              # Filling max height from right to left

        result=0                       
        for i in range(n):              
            result+=min(left[i], right[i])-height[i]   # from max height of both array, getting the min height and subtracting it with current height to get the result
        return result


        """
        Tc: 0(n)
        Sc: 0(n)

        how are we calculating result+=

        - By running through the left and right array from left to right, we will get min height from both array,
        why min height? Because at current index we will get min height (either from right or left) and subtract it from current height

        - how result is 0 at index 3? at index 3 height is 2 and min height from left and right is also 2 so 2-2 =0
        - How result is 1 at index ? at index 4 the max height from left arr is 2 and max height from right arr is 3, we will 
        get min of 2 and 3, which is 2 and current height at index 4 is 1 so: 2-1:1
        - So the result is 1 because 1 level of water will be getting stored
        """