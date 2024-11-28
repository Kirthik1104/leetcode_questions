class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n   # [1,1,1,1]
        right=[1]*n  # [1,1,1,1]
        left_product=1
        right_product=1
        for i in range(len(nums)):
            
            
            left[i]=left_product   # Filling the elements from left to right
            left_product*=nums[i]   # calcualting the current product to left which will be inserted in the next pos
            
            j=-i-1     # starts from reverse to start if i is 0, j is -0-1 which is -1 then -2, -3, -4
            right[j]=right_product # Filling the elements from right to left
            right_product*=nums[j]  # Calculating the current product to right which will be inserted in next pos
            
            
        return ([l*r for l,r in zip(left, right)])  # returning new list by mult both values from left and right



        """
        tIME COMEPLEXITY: o(N)
arr = [5, 4, 3, 2]
First pass (Left Products):
---------------------------
Iteration 1 (i = 0):
left[0] = left_product = 1  -->Because no element is present before left[0] so left is set to 1
Update left_product = left_product * arr[0] = 1 * 5 = 5  --> calculating product for index1 which is: left product*index[0]
State after iteration 1:
css
Copy code
left = [1, 1, 1, 1]
left_product = 5

Iteration 2 (i = 1):
left[1] = left_product = 5
Update left_product = left_product * arr[1] = 5 * 4 = 20
State after iteration 2:
css
Copy code
left = [1, 5, 1, 1]
left_product = 20

Iteration 3 (i = 2):
left[2] = left_product = 20
Update left_product = left_product * arr[2] = 20 * 3 = 60
State after iteration 3:
css
Copy code
left = [1, 5, 20, 1]
left_product = 60

Iteration 4 (i = 3):
left[3] = left_product = 60
Update left_product = left_product * arr[3] = 60 * 2 = 120
State after iteration 4:
css
Copy code
left = [1, 5, 20, 60]
left_product = 120

Second pass (Right Products):
-----------------------------
Iteration 1 (i = 0, j = -1):
right[-1] = right_product = 1 (right[3])
Update right_product = right_product * arr[-1] = 1 * 2 = 2
State after iteration 1:
css
Copy code
right = [1, 1, 1, 1]
right_product = 2

Iteration 2 (i = 1, j = -2):
right[-2] = right_product = 2 (right[2])
Update right_product = right_product * arr[-2] = 2 * 3 = 6
State after iteration 2:
css
Copy code
right = [1, 1, 2, 1]
right_product = 6

Iteration 3 (i = 2, j = -3):
right[-3] = right_product = 6 (right[1])
Update right_product = right_product * arr[-3] = 6 * 4 = 24
State after iteration 3:
css
Copy code
right = [1, 6, 2, 1]
right_product = 24

Iteration 4 (i = 3, j = -4):
right[-4] = right_product = 24 (right[0])
Update right_product = right_product * arr[-4] = 24 * 5 = 120
State after iteration 4:
css
Copy code
right = [24, 6, 2, 1]
right_product = 120


Final Step: Multiply Left and Right Products
------------------------------------------------

Now we multiply the corresponding elements of left[] and right[] to get the final result:

Index 0: output[0] = left[0] * right[0] = 1 * 24 = 24
Index 1: output[1] = left[1] * right[1] = 5 * 6 = 30
Index 2: output[2] = left[2] * right[2] = 20 * 2 = 40
Index 3: output[3] = left[3] * right[3] = 60 * 1 = 60


output = [24, 30, 40, 60]

        """
