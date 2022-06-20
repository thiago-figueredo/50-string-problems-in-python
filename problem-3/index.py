# Problem 3 (Easy): Roman to Integer.

# romanToInt(roman_number: str) -> int
# 1) Maintain a hash table (roman_table) with roman numerals as keys and their 
# corresponding integer values as values.
# 2) Declare a variable called int_value to be returned and initialize it to 0.
# 3) Iterate through roman_number, and pattern match current character and next character in a tuple.
# (current_char, next_char) = (roman_number[i], roman_number[i+1])
# 4) Check if tuple matches ("I", "V" | "X") | ("X", "L" | "C") | ("C", "D" | "M")
# 5) If tuple matches, add roman_table[next_char] - roman_table[current_char] to int_value 
# and increment index i by 2.
# 6) Else, if roman_table[current_char] is in the roman_table, add it to int_value and increment index i by 1.
# 7) Then, after the loop return int_value.

# Space Complexity: O(1)
# Time Complexity: O(n)

def romanToInt(roman_number: str) -> int:
  roman_table = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
  }

  int_value = 0
  str_len = len(roman_number)
  i = 0

  while i < str_len:
    current_char = roman_number[i]
    next_char = roman_number[i+1] if i+1 < str_len else None

    match (current_char, next_char):
      case ("I", "V" | "X") | ("X", "L" | "C") | ("C", "D" | "M"):
        int_value += roman_table[next_char] - roman_table[current_char]
        i += 2
      case _ if roman_number[i] in roman_table:
        int_value += roman_table[roman_number[i]]
        i += 1

  return int_value
