from index import intToRoman

def test_problem4_solution():
  assert intToRoman(1) == "I"
  assert intToRoman(2) == "II"
  assert intToRoman(3) == "III"
  assert intToRoman(4) == "IV"
  assert intToRoman(5) == "V"
  assert intToRoman(6) == "VI"
  assert intToRoman(7) == "VII"
  assert intToRoman(8) == "VIII"
  assert intToRoman(9) == "IX"
  assert intToRoman(10) == "X"
  assert intToRoman(49) == "XLIX"
  assert intToRoman(50) == "L"
  assert intToRoman(99) == "XCIX"
  assert intToRoman(100) == "C"
  assert intToRoman(499) == "CDXCIX"
  assert intToRoman(500) == "D"
  assert intToRoman(999) == "CMXCIX"
  assert intToRoman(1000) == "M"
  assert intToRoman(1994) == "MCMXCIV"

if __name__ == '__main__':
  test_problem4_solution()