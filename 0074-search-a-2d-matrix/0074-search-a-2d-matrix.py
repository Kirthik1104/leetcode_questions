class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Binary Search

        for each_array in matrix:
        
            left=0
            right=len(each_array)-1

            
    
            while left<=right:
                mid=(left + right)//2
                
                if each_array[mid]==target:
                    return True
                elif target> each_array[mid]:
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