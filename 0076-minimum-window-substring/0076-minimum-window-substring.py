class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count = {}
        if not t or not s:
            return ""

        # Character count of t
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1

        # Total unique count of chars in char_count
        required = len(char_count)

        # Formed: total characters present in t 
        formed = 0

        # Determining the window pointer
        left, right = 0, 0

        # Dictionary to keep track of occurrences of chars in the window sizes formed
        window_count = {}

        # To track the length of the minimum window
        min_length = float('inf')

        # Result: Used to store the result
        result = ""

        while right < len(s):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            if char in char_count and window_count[char] == char_count[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                # Update result if this window is smaller
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left: right + 1]

                # Remove character from the left
                window_count[char] -= 1
                if char in char_count and window_count[char] < char_count[char]:
                    formed -= 1

                left += 1

            # Move the right pointer
            right += 1

        return result 