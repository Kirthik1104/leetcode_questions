class Solution:
    def simplifyPath(self, path: str) -> str:

        """
        Summary
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        path = path.split("/")  # Split the string with delimeter as / (if // is encountered, it will still assume single  "")--> Result is a list of chars
        directory=[]           # creating a stack
        for char in path:
            if char == "" or char == ".":  # Acces the list of chars and continue if its a empty space or a single directory
                continue 
            elif directory and char == "..":  # check if directory has elements, only then pop the last element when the char is ..
                directory.pop()
            elif not directory and char == "..": # if dictionary is empty and you encounter a  .. continuue
                continue
            else:
                directory.append(char) # for rest other append (text, ...)
 
        return ("/"+"/".join(directory)) # "/"+ add slash in front, convert the list of chars to a string with / between them and return 
                