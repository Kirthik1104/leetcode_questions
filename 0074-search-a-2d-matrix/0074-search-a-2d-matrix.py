class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """
        1) The idea is to conceptually flattenning the 2d matrix to 1d array and running a while loop from 0 to row * column -1

        2) getting mid point in 1d array, and using this formula to trace the position of element midpoint in the 2d matrix

        3) mid: gives mid value at 1d array. 

              3.1) mid//column---> Gives row number (//) is quotient

              3.2) mid%column--- > Gives the column number (%) is remainder

              why do divide and modulus by column no--> if size of each column is 4 (0,3)
              index 0//4=0, index 1//4=0, index 2//4=0, index 3//4=0, row=0
              index 4//4=1, index 5//4=1............................. row=1

              index 0%0= 0 column, index 1%4 = 1 column, index 2%4 = 2 column, index3%4 = 3 column

        """

        row=len(matrix)
        column=len(matrix[0])

        left=0
        right= row * column - 1
      
        while left<=right:
            mid=(left + right)//2
       
            mid_value = matrix [mid//column][mid%column]  # getting row and column of mid
      

            if mid_value==target:
                return True
            elif target> mid_value:
                left = mid+1
            else:
                right = mid-1
        return False

        # Bruet Force:

        # for each_array in matrix:
        #     for each_val in each_array :
        #         if each_val==target:
        #             return True
        # return False