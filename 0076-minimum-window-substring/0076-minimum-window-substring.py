class Solution:
    def minWindow(self, s: str, t: str) -> str:

        """
        1) Steps to solve:

        Take 1 hashmap for t and store all the occurence of chars along with the number of occurence
        required_len = Use a varibale to get the count of unique character element of t

        Take 1 hashmap for s and and and start from a window (left and traverse till right), and store all the occurence of chars with the occurence number
        from the occurence of all chars, use a variable to only store the same occurence of chars in both the hasmap---> used to signify same chars have been found in current window size
        formed_len =  use a variable to only store the same occurence of chars in both the hasmap---> used to signify same chars have been found in current window size

        required_len = formed_len ---> All elemnts of t are present in the current window size. ---> Shrink the window from left---> Also when shrinking if one of the matching char of t gets 
        removed from window, make sure to update the count in hashmap and also ---> decrement the count of formed_len---> to signify that matching elemnts has been removed from left
        and we need to move right unless and untill we have all the chars of t in the current window size
        """

        if not t or not s:
             return ""
        
        # 1) Hashmap to get the occurence of chars in t and the occurence number
        char_count_t = {}

        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        # 1.1) Variable to store the character length of t
        required_len = len(char_count_t)

        # 2) Hashmap to store the char and its occurence in the current window size
        window_char_count = {}

        # 2.1) Varibale used to store the occurence of the same char count of occurence in t with s
        formed_len = 0

        # 3) Pointers to traverse
        left, right = 0,0

        # 4) Result to store the string
        result=""

        # To track the length of the minimum window
        min_length = float('inf')


        # while loop to traverse the chars in s
        while right < len(s):
            char = s[right]
            window_char_count[char] =  window_char_count.get(char, 0) + 1  # filling the hashmap with chars and occurence

            # This part also handles duplicates elements and carefully checks the count in both the hashmaps, checks if present and occurence ---> only then it updates the formed variable
            if char in char_count_t and char_count_t[char] == window_char_count[char]: #checking if char is present in char_count hasmap and if it has same no. of occurence. if yes update the formed
                formed_len+=1

            # if all the chars of t and present in the current window with cocrrect no of occurence, we will store the string formed in a result and comapre for min_length as we build the string.
            while left<=right and formed_len == required_len:
                char = s[left]

                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    result = s[left : right+1]

                # Shrinking stage -- > before skrinking we need to update the count of occurence of chars in window_size and
                window_char_count[char] -= 1

                # also check if matching elements of both string is also removed while shrinking, if yes then update the formed_length count as well
                if char in char_count_t and window_char_count[char] < char_count_t[char]:
                    formed_len-=1
                left+=1  # shrinkg the window

            right+=1 # all chars of t are currently not in the window, keep going right

        return result                









       