class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid=[]

        for index1, trans1 in enumerate(transactions):
            name1, time1, amount1, city1 = trans1.split(",")

            if int(amount1)>1000:
                invalid.append(trans1)
                continue

            for index2, trans2 in enumerate(transactions):
                if index1!=index2:

                    name2, time2, amount2, city2 = trans2.split(",")

                    if name1==name2 and city1!=city2 and abs(int(time1) - int(time2))<=60:
                        invalid.append(trans1)
                        break
        return invalid
