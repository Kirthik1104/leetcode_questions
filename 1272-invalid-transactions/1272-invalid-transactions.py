from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = set()  # Use a set to avoid duplicate invalid transactions
        parsed = []  # Store parsed transactions
        
        # Parse transactions into a list of tuples: (name, time, amount, city, index)
        for i, transaction in enumerate(transactions):
            name, strtime, amount, city = transaction.split(",")
            parsed.append((name, int(strtime), int(amount), city, i))
        
        # Check each transaction against others
        for i, (name1, time1, amount1, city1, idx1) in enumerate(parsed):
            if amount1 > 1000:  # Rule 1: Amount exceeds $1000
                invalid.add(idx1)
            
            for j, (name2, time2, amount2, city2, idx2) in enumerate(parsed):
                # Rule 2: Check for same name, time within 60 minutes, and different cities
                if i != j and name1 == name2 and abs(time1 - time2) <= 60 and city1 != city2:
                    invalid.add(idx1)
                    invalid.add(idx2)
        
        # Collect transactions marked as invalid
        return [transactions[i] for i in invalid]
