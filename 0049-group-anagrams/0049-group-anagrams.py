from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict=defaultdict(list)

        for chars in strs:
            count=[0]*26
            
            for char in chars:
                count[ord(char)-ord('a')]+=1
            
            mydict[tuple(count)].append(chars)
            
        return ([values for values in mydict.values()])

        



















   

        # freq={}
        # for char in strs: # go throug each char in list

        #     sorted_char=sorted(char)  # sort each string. eat becomes aet

        #     key=tuple(sorted_char)  #convert string to tuple so that it becoomes immutable 

        #     if  key not in freq:  # check if key exists. if not then create and assign original string in list
        #         freq[key]=[char]
        #     else:
        #         freq[key].append(char) # if already exists. append it
        # return list(freq.values())   # return it in the form of list fo values 

        # freq=defaultdict(list)
        # for string in strs: # go throug each char in list
        #     count=[0]*26  
        #     for char in string:
        #         count[ord(char)-ord('a')]+=1 

        #     freq[tuple(count)].append(string)

        # return list(freq.values())
        # # anagram=defaultdict(list)
        # # result = []

        # # for s in strs:
        # #     sorted_s=tuple(sorted(s))
        # #     anagram[sorted_s].append(s)
        # # for value in anagram.values():
        # #     result.append(value)
        # # return result
                

        

        # """
        # 1. Character Counting Approach (Using ord())
        # -------------------------------------
        # Time Complexity: O(N * K)
        # N: Number of strings in the input list.
        # K: Average length of the strings.
        # Explanation: For each string, we count the occurrences of each character in linear time (O(K)) and store the results in a dictionary. The dictionary operations (insertion and lookup) are average O(1).

        # 2. Sorting Approach
        # ---------------------------
        # Time Complexity: O(N * K log K)
        # N: Number of strings in the input list.
        # K: Average length of the strings.
        # Explanation: For each string, we sort it, which takes O(K log K) time. We then use the sorted string as a key in the dictionary. The sorting step is what introduces the logarithmic factor, making this approach less efficient than character counting.
        #         """


