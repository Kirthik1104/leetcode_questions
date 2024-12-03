class OrderedStream:

    def __init__(self, n: int):
        self.result = [""] * n  # Initialize stream with empty strings
        self.pointer = 0  # Start pointer at the beginning

    def insert(self, idKey: int, value: str) -> List[str]:
        self.result[idKey - 1] = value  # Insert the value at the correct position
        output = []

        # Collect all contiguous elements starting from the pointer
        while self.pointer < len(self.result) and self.result[self.pointer] != "":
            output.append(self.result[self.pointer])
            self.pointer += 1  # Move the pointer forward

        return output



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


"""
Explanation of List of Lists
Here’s the step-by-step breakdown of how the outputs are combined into a single list of lists:

Initialization:

The constructor (OrderedStream(5)) is called.
In the framework, this is represented by null in the result list.
First Insert:

obj.insert(3, "ccccc") returns [].
This is appended to the result list: [null, []].
Second Insert:

obj.insert(1, "aaaaa") returns ["aaaaa"].
This is appended to the result list: [null, [], ["aaaaa"]].
Third Insert:

obj.insert(2, "bbbbb") returns ["bbbbb", "ccccc"].
This is appended to the result list: [null, [], ["aaaaa"], ["bbbbb", "ccccc"]].
Fourth Insert:

obj.insert(5, "eeeee") returns [].
This is appended to the result list: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], []].
Fifth Insert:

obj.insert(4, "ddddd") returns ["ddddd", "eeeee"].
This is appended to the result list: [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]].

Summary
--------
The insert function always returns a single list (either empty or containing contiguous elements).
The list of lists structure in the output is created by the test framework or driver code aggregating the results of multiple calls.
The null corresponds to the constructor call (__init__), and each subsequent list corresponds to the output of an individual insert call.

"""