from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time_range(speed: int)->bool:
            times_spent_to_eat_allbananas=0
            for pile in piles:
                times_spent_to_eat_allbananas += ceil(pile/speed)
            return times_spent_to_eat_allbananas <= h


        """
        1) The goal is to find a minimum speed (k) which could eat all bananas in all piles under time h

        2) valid speeds are 1 and max value of piles (just for consideration)

        3) Do not get confused with the values in piles with the speed calcation, those are not related.
        4) we will calculate a middle speed withn this range 1+11/2= 6
        5) call def time_range fucntion with speed 6. we will divide total no. of bananas in each pile with this speed using a ceil.

        Ceil will round off the decimal value. ceil(3/6)=1 hour to eat 3 bananas, ceil(6,6)=1 hour, ceil(7/6)=2 hour, ceil(11/6)=2 
        hours..-> 1+1+2+2 which is 6<=8. 6 is (is diffdrent and our speed 6 is different) also valid because in speed 6 it finished 
        eating all bananas in less than 8 hours----> Now very important--> if 6 is valid becasue it is less than 8 then speed which
        is less than 6 is also valid?-> Yes!!. then the return statement will return True and read from below

        so we will check if time spent to eaat all bananas in speed 6 is less than the given time which 8, then there mist be speed which is less
        than 6 which can eat all bananas under the given time 8.it returns true and to decrease the speed, we will decrement speed by 1 and repeat 
        the while loop again speed is now 6-1= 5. 1+5/2 = 3

        call the fucntion with 3. times will be >10 this is not valid. because at speed 3 it is taking more time than given time 8 to complete all
        bananas. so we will increse the speed by 1 by increment low.
        """
        

        # `left` is the minimum speed (1 banana per hour),
        # `right` is the maximum speed (max pile size, eating one pile in 1 hour).
        low = 1
        high = max(piles)

         # Initialize the result to the maximum possible speed
        result = high
        while low<=high:
            # Calculate the middle speed of the current range
            speed = (low + high)//2

            # Check if Koko can finish all bananas at the current speed
            if time_range(speed):
                 # If yes, update the result to the current speed
                result = speed
                # Look for a smaller valid speed in the left half
                high = speed - 1
            else:
                # If not, increase the speed and look in the right half
                low = speed + 1
        return result

        """
        Since we do a full loop over the piles for every step in the binary search, the total complexity is: O(n⋅log(max(piles)))
        n: Number of piles.
        log(max(piles)): Number of binary search steps.
        """