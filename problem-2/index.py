# Problem 2 (Easy): Write a function to find the longest common prefix string 
# amongst an array of strings. If there is no common prefix, return an empty string "".

from typing import List

# longestCommonPrefix(strs: List[str]) -> str
# 1) Declare the longest_common_prefix variable to be returned;
# 2) Declare a hash map to store the characters of each string;
# 3) If strs has only one element, return it;
# 4) Else, loop over each string in strs;
# 5) Loop over each character of current string;
# 6) If current character is not in the hash map at the key index, add it; (hash_map[index] = string[index])
# 7) Else, append it to hash map; (hash_map[index] += string[index])	
# 8) Then, loop over each value of hash map;
# 9) Check, if the first element of value it's not repeated lenght of strs times and 
# value has less or equal than one element; (if value.count(value[0]) != len(strs) or len(value) <= 1)
# 10) If so, break the loop;
# 11) If not, append first element of value to longest_common_prefix;
# 12) Return longest_common_prefix;

# Space Complexity -> O(n)
# Time Complexity -> O(n^2)

def longestCommonPrefix(strs: List[str]) -> str:
  longest_common_prefix = ""
  hash_map = {}

  match strs:
    case [x]: return x
    case [*_]: 
      for string in strs:
        string_len = len(string)

        for index in range(string_len):
          if index in hash_map:
            hash_map[index] += string[index]
          else:
            hash_map[index] = string[index]

      for value in hash_map.values():
        element = value[0]

        if value.count(element) != len(strs) or len(value) <= 1:
          break

        longest_common_prefix += element
      
  return longest_common_prefix
