## 50 String Problems in Python
The Difficulty rating is based on leetcode.

## Requirements: 
- python 3.10 

***
<br />

https://leetcode.com/problems/reverse-words-in-a-string
## Problem 1 (Medium): Given an input string s, reverse the order of the words. 
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string o the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

### Example 1:
>Input: s = "the sky is blue" \
>Output: "blue is sky the"
### Example 2:

>Input: s = "  hello world  " \
>Output: "world hello" \
>Explanation: Your reversed string should not contain leading or trailing spaces.
### Example 3:

>Input: s = "a good   example" \
>Output: "example good a" \
>Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
### Constraints:
>- 1 <= s.length <= 104
>- s contains English letters (upper-case and lower-case), digits, and spaces ' '.
> - There is at least one word in s.
 
> Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space? 
***
<br />

https://leetcode.com/problems/longest-common-prefix/
## Problem 2 (Easy): Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".

### Example 1:

> Input: strs = ["flower", "flow", "flight"] \
> Output: "fl" \
> Example 2:

### Example 2:

> Input: strs = ["dog", "racecar", "car"] \
> Output: "" \
Explanation: There is no common prefix among the input strings.
 
### Constraints:

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters.
***
<br />