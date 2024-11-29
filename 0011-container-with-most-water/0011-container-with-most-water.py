class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        Two Pointer: Tc O(n)
        why Two pointer?
        ------------------
        - If height at either pointer position is highest than we will keep it constant and move the other pointer so that we get the matching height or close to highest height.

        width= horizantal distance btw indexes (i, j): area= (j-1)* min(height[left], height[right])
        why min? because if either height at pointer is smaller than the other one, than the heights are slanted.
        thats why we take min height of both and multiply it with difference of horizantal distance to get area.
        """
        left=0
        right=len(height)-1
        res=0
        while left<right:

            area=(right-left)*min(height[left], height[right])
            res=max(res, area)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res







        """
        Brute force
        ----------
        Time complexity: O(n^2)


    right-left:- The width is simply the difference between the indices of the two lines, which gives us the horizontal distance.

min(height[left],height[right]):-area is determined by multiplying this width by the shorter height of the two lines, as the container cannot hold more water than the height of the shorter line.

       """

        # res=0

        # for left in range(len(height)):               
        #     for right in range(left+1, len(height)):
        #         area=(right-left)*min(height[left],height[right])
        #         res=max(res, area)
        # return res




#         """

#          Two pointer:

#          1) Compare position at leftt with right
#          2 Calculate the area
#          3) Check if height at left is smaller than right move left to right else move right to left
#          4) Time complexxity o(n):-- only using 1 for loop
#         """

#         left=0
#         right=len(height)-1

#         result=0
        
#         while left<right:    # Pointer to keep traversing in x axis


#             # area=(breadt* min (height at left, height at right))
#             area=(right-left)* min(height[left], height[right])  

#             result=max(result, area)

#             if height[left]<height[right]:  # to check if height at left is smaller than right
#                 left+=1       # if height is smaller inleft. Move left one position to right
#             else:
#                 right-=1  # Move right one position to left


#         return result  # return the result stored






        