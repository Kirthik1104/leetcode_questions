from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
          1. Sorting Approach
        ---------------------------
        Time Complexity: O(N * K log K)
        Space Complexity: O(n*k):  The space required for storing keys and values is O(n⋅k), as each string and its frequency count are stored in memory.
        N: Number of strings in the input list.
        K: Average length of the strings.
        Explanation: For each string, we sort it, which takes O(K log K) time. We then use the sorted string as a key in the dictionary. The sorting step is what introduces the logarithmic factor, making this approach less efficient than character counting.
                """

        freq={}
        for char in strs: # go throug each char in list

            sorted_char=sorted(char)  # sort each string. eat becomes aet

            key=tuple(sorted_char)  #convert string to tuple so that it becoomes immutable 

            if  key not in freq:  # check if key exists. if not then create and assign original string in list
                freq[key]=[char]
            else:
                freq[key].append(char) # if already exists. append it
        return list(freq.values())   # return it in the form of list fo values 

       

        """
         2. Character Counting Approach (Using ord())
        -------------------------------------
        Time Complexity: O(N * K)
        Space Complexity: O(n*k):  The space required for storing keys and values is O(n⋅k), as each string and its frequency count are stored in memory.
        N: Number of strings in the input list.
        K: Average length of the strings.
        Explanation: For each string, we count the occurrences of each character in linear time (O(K)) and store the results in a dictionary. The dictionary operations (insertion and lookup) are average O(1).
        """
        mydict=defaultdict(list)

        for chars in strs:
            count=[0]*26        #creating list of 26 zeroes
            
            for char in chars:
                count[ord(char)-ord('a')]+=1  #appending 1's to count list
            
            mydict[tuple(count)].append(chars)  #converting count list to tuple to use it as a key. if same values found append the chars
            
        return ([values for values in mydict.values()]) # return lift of list of values

      

