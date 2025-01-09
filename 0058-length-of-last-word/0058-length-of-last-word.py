class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Tc: O(n): split O(N), -1 O(1), len(lastword) is O(k). Overall O(n)

        return len(s.split()[-1])   #--> Split: Removes all space and create a list of words. -1 access last word, len gives length of last word

        # for empty s=""  (input is greater than 0r equal to 1) but in this case put a if condition: if not s: return False
        