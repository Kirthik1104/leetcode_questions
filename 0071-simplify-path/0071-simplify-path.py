class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        directory=[]
        for char in path:
            if char == "":
                continue
            elif char == ".":
                continue
            elif directory and char == "..":
                directory.pop()
            elif not directory and char == "..":
                continue
            else:
                directory.append(char)
 
        return ("/"+"/".join(directory))
                