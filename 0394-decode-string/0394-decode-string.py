class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_str = ""
        curr_num = 0

        for char in s:
            if char.isdigit():  # Build the current number
                curr_num = curr_num * 10 + int(char)
            elif char == '[':  # Push current string and number to stacks
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_str = ""  # Reset for the new scope
                curr_num = 0
            elif char == ']':  # Pop from stacks and build the decoded string
                repeat_times = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + (curr_str * repeat_times)
            else:  # Append character to current string
                curr_str += char

        return curr_str