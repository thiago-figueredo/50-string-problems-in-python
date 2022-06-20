from index import romanToInt

def test_problem3_solution():
  assert romanToInt("III") == 3
  assert romanToInt("LVIII") == 58
  assert romanToInt("MCMXCIV") == 1994
  assert romanToInt("DCXXI") == 621

if __name__ == "__main__":
  test_problem3_solution()