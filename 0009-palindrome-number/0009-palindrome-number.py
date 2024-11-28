class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original=x            # coping x to original number
        reverse=0             # starting reverse with 0

        while x>0:            # x will be decreased in every iteration, it will run till its greater than 0
            digit=x%10        # anything %10 gives the last number. % is a remainder
            reverse=reverse * 10 + digit  # shifts the position by 10's place everytime
            x//=10            # //10 removes last number. // is quotient, gives rounded value
        return original==reverse


        """
        Example Execution (x = 121):
        Initial Setup:

        original = 121
        reversed_num = 0

        First Iteration:
        Extract last digit: digit = 121 % 10 = 1.
        Update reversed_num: reversed_num = 0 * 10 + 1 = 1.
        Remove last digit from x: x = 121 // 10 = 12.

        Second Iteration:
        Extract last digit: digit = 12 % 10 = 2.
        Update reversed_num: reversed_num = 1 * 10 + 2 = 12.
        Remove last digit from x: x = 12 // 10 = 1.

        Third Iteration:
        Extract last digit: digit = 1 % 10 = 1.
        Update reversed_num: reversed_num = 12 * 10 + 1 = 121.
        Remove last digit from x: x = 1 // 10 = 0.

        End of Loop:
        x becomes 0, and the loop stops.
        reversed_num = 121.
        Comparison:

        Compare original (121) with reversed_num (121).
        Since they are equal, the function returns True.

        """
        

        

        