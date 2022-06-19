# The solution to be tested is the most efficient one.

from index import reverseWordsConstantSpace

def test_problem_1_solution():
  assert reverseWordsConstantSpace("the sky is blue") == "blue is sky the"
  assert reverseWordsConstantSpace("  hello world  ") == "world hello"
  assert reverseWordsConstantSpace("a good   example") == "example good a"

if __name__ == '__main__':
  test_problem_1_solution()