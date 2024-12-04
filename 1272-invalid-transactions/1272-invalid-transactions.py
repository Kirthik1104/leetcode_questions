class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=[]
        hashmap=defaultdict(dict)
        for transaction in transactions:
            name, strtime, amount, city = transaction.split(",")
            time=int(strtime)
            
            if name not in hashmap[time]:   # { time : {name :{city}}}--> Check if name does not exits for current time
                hashmap[time][name]={city}  #{city}: storing city as a set to not include duplicates
            if name in hashmap:
                hashmap[time][name].add(city)
                
                
        for curr in transactions:
            
            name, strtime, amount, city = curr.split(",")
            time=int(strtime)
            
            if int(amount)>1000:   # if amount for current transaction is above 1000, add it to invalid and continue to go to next iteration of curr
                invalid.append(curr)
                continue    # if this satisfies, then dont go down instead go to next transaction using continue
            
            # From current time and name from 1st loop will compare all possible same name, with same or different time and different city for invalid transaction ( from current time we will check current time -60 and current time + 60 for possible invalid transactions)
            
            for intervals in range(time-60, time+61): # next transaction time can be 60 min less than curr time or 60 min more than current time.
            #     transaction_time = {
            #     20: {"alice": {"mtv", "sf"}}, [time][name]={city}
            #     40: {"alice :{"beijing"}}
            #     50: {"alice": {"beijing"}}
            #     50: {"bob": {"mtv"}}
            # }
                
            # Inner loop will run for 60 sides on either sides and take name and time from 1st loop and compare againts all names and time in the range
            # check if current time or next interval exits in hashmap
                if intervals in hashmap and name in hashmap[intervals]:
                    cities=hashmap[intervals][name]
                    
                """
                    1st if condition below: 
                    ---------------------
                    # 40: {"alice :{"mtv"}}
                    # 50: {"alice": {"beijing"}} 
                    
                    outer loop: trans1
                        inner loop (0..trans1...60)
                    
                    if trans 1 is in 1st for loop and second for loop check range in (+_60) which has second transaction.
                    for second transaction whihc is in the range of  time, cities will have beijing and current city is still mtv, both are !=.
                    Invalid found and break immdetely no need to check further for next invalid
                    
                    2nd if condition below:
                    ----------------------
                    
                    20: {"alice": {"mtv", "sf"}}, 
                    
                    since len of cities is 2. invalid bevause different city for same name and same time
                    
                """
                    if city not in cities or len(cities)> 1:
                        invalid.append(curr)
                        break
        return invalid
            


        """
        Brute: O(n2)
        """

        invalid=[]

        for index1, trans1 in enumerate(transactions):
            name1, time1, amount1, city1 = trans1.split(",")

            if int(amount1)>1000:
                invalid.append(trans1)
                continue                        # if any transaction has amount > 1000 go to next transanctions

            for index2, trans2 in enumerate(transactions):
                if index1!=index2:

                    name2, time2, amount2, city2 = trans2.split(",")

                    if name1==name2 and city1!=city2 and abs(i0nt(time1) - int(time2))<=60:
                        invalid.append(trans1)
                        break
        return invalid


        """
        1. Reason for break:

        Once trans1 is identified as invalid, we don’t need to compare it with other transactions because:It’s already marked as invalid.
        Appending trans1 multiple times to the invalid list (or set) for different reasons is unnecessary.

        2. Why Are We Appending trans1 Instead of trans2?
        Context:

        We’re iterating through transactions using the outer loop (trans1) and comparing it with other transactions (trans2).
        The goal is to determine whether trans1 itself is invalid.


        Why Does len(cities) > 1 Matter?
        This condition ensures:

        Multiple-City Transactions Are Detected:

        At time = 20, "alice" transacted in two cities: {"mtv", "beijing"}.
        This violates the problem constraints, so all transactions at this time for "alice" are marked invalid.
        Efficient Multi-City Detection:

        Using a set for cities ensures duplicate cities are ignored (e.g., two transactions in "mtv" at the same time wouldn’t trigger this condition).

        """



