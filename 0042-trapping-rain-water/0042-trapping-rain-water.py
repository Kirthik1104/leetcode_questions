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

        """