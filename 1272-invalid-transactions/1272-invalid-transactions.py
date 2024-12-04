class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=[]

        for index1, trans1 in enumerate(transactions):
            name1, time1, amount1, city1 = trans1.split(",")

            if int(amount1)>1000:
                invalid.append(trans1)
                continue                        # if any transaction has amount > 1000 go to next transanctions

            for index2, trans2 in enumerate(transactions):
                if index1!=index2:

                    name2, time2, amount2, city2 = trans2.split(",")

                    if name1==name2 and city1!=city2 and abs(int(time1) - int(time2))<=60:
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

        """
