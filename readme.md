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

https://leetcode.com/problems/roman-to-integer/
## Problem 3 (Easy): Roman to Integer.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

>Symbol       Value \
I       ->     1 \
V       ->     5 \
X       ->      10 \
L       ->     50 \
C       ->      100 \
D       ->      500 \
M       ->      1000 

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

### Example 1:

>Input: s = "III" \
Output: 3 \
Explanation: III = 3. 

### Example 2:

> Input: s = "LVIII" \
Output: 58 \
Explanation: L = 50, V= 5, III = 3. 

### Example 3:

> Input: s = "MCMXCIV" \
Output: 1994 \
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4. 
 
### Constraints:

- 1 <= s.length <= 15 
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').  
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].