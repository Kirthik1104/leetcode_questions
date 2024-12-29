class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        n=len(matrix)

        for each_array in matrix:
            for each_val in each_array :
                if each_val==target:
                    return True
        return False
        