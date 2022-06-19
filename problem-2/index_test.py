from index import longestCommonPrefix

def test_problem_2_solution():
  assert longestCommonPrefix(["dog", "racecar", "car"]) == ""
  assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
  assert longestCommonPrefix(["dog", "django", "dj"]) == "d"
  assert longestCommonPrefix(["d", "d", "d"]) == "d"
  assert longestCommonPrefix(["cir", "car"]) == "c"
  assert longestCommonPrefix(["aaa", "aa", "aaa"]) == "aa"

if __name__ == '__main__':
  test_problem_2_solution()