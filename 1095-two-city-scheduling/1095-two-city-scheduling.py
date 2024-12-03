class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        """
        Tc: Nlognn for sorting

        1) Key Insight:

        The main goal is to minimize the total cost of sending \U0001d45b people to City A and \U0001d45b people to City B.

        Eg: 1
        Step1:
        -------
        10, 20: for City A -10 cost required less as compared to City B
        30, 200 For city A -170 cost required less as compared to City B
        400, 50 For City B -350 cost required less as compared to City A
        30, 20 For City B -10 cost reuiqred less as compared to City A
        Step2:
        ------
        Sort the array of people by this difference in ascending order-->
        People who save the most by going to City A appear at the start.
        People who save the most by going to City B appear at the end.

        After sorting: The first n people in the sorted list are assigned to City A-->These are the people with the smallest differences or the largest savings when sent to City A.

        The remaining n people (second half of the sorted list) are assigned to City B-->These are the people with the largest differences or the largest savings when sent to City B.

        A negative difference (A - B < 0) implies that sending the person to City A is cheaper.
        A positive difference (A - B > 0) implies that sending the person to City B is cheaper.

        Step 3: How for loop is assigned: for any length. First half will go for city A. Second half will go for city B. Check above explanation
        """


        costs.sort(key=lambda pair: pair[0]-pair[1])

        n=len(costs)
        result=0
        for i in range(n//2):
            result+=costs[i][0]    # [i][0]-->00, 10, 20--> Takes first element which is sorted according to minimum cost
        for i in range(n//2, n):   
            result+=costs[i][1]    # [i][1]-->(from half start accessing second element ot get city b) 
        return result

