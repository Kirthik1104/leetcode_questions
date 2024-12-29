class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Binary Search

        row=len(matrix)
        column=len(matrix[0])

        left=0
        right= row * column - 1
        print(right)
        while left<=right:
            mid=(left + right)//2
            print(mid)
            mid_value = matrix [mid//column][mid%column]
            print(mid_value)

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