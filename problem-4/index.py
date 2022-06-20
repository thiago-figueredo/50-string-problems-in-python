# Problem 4 (Medium): Integer to Roman.

# intToRoman(num: int) -> str
# 1) Declare a roman number variable to be returned and initialize it to an empty string. 
# 2) Maintain a dictionary of roman numerals and their corresponding values in decrescent order. 
# 3) Iterate over key, value in the roman dictionary.
# 4) While num - value >= 0, add the key to the roman number string 
# and subtract value from num. 
# 5) After roman dictionary loop, return the roman number string.

# Space Complexity -> O(1)
# Time Complexity -> O(n)

def intToRoman(num: int) -> str:
  roman_number = ""
  roman_table = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
  }
  
  for key, value in roman_table.items():
    while num - value >= 0:
      roman_number += key
      num -= value
          
  return roman_number