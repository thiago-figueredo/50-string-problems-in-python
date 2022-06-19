# reverseWordsLinearSpace(word: str, delimiter: str = " ") -> str:
# 1) Declare a variable splitted_word which is the result of removing delimiter 
# from the start and end of word, and splitting it by delimiter; 
# (splitted_word = word.strip(delimiter).split(delimiter))
# 2) Split word by delimiter;
# 3) Declare a empty string reversed_word to be returned;
# 4) Loop over each character of word starting from the end to start appending current char to word;
# 5) If current index (i) is less than input length - 1 and current char is not "", append delimiter to word; 
# 6) Else, do nothing;
# 7) Then, return reversed_word;

# Space Complexity -> O(n)
# Time Complexity -> O(n)

def reverseWordsLinearSpace(word: str, delimiter: str = " ") -> str:
  splitted_word = word.strip(delimiter).split(delimiter)
  splitted_word_len = len(splitted_word)
  reversed_word = ""

  for i in range(splitted_word_len):
    index = splitted_word_len - i - 1
    character = splitted_word[index]
    reversed_word += character

    if i < splitted_word_len - 1 and character != "":
      reversed_word += delimiter

  return reversed_word

# reverseWordsConstantSpace(word: str, delimiter: str = " ") -> str:
# 1) Declare a variable splitted_word which is the result of removing delimiter 
# from the start and end of word, and splitting it by delimiter; 
# (splitted_word = word.strip(delimiter).split(delimiter))
# 2) Set word to empty string; 
# 3) Loop over each character of word starting from the end to start, appending current char to word;
# 4) If current index (i) is less than input length - 1 and current char is not "", append delimiter to word; 
# 5) Else, do nothing;
# 6) Then, return reversed_word;

# Space Complexity -> O(1)
# Time Complexity -> O(n)
def reverseWordsConstantSpace(word: str, delimiter: str = " ") -> str:
  splitted_word = word.strip(delimiter).split(delimiter)
  splitted_word_len = len(splitted_word)
  word = ""

  for i in range(splitted_word_len):
    index = splitted_word_len - i - 1
    character = splitted_word[index]
    word += character

    if i < splitted_word_len - 1 and character != "":
      word += delimiter

  return word