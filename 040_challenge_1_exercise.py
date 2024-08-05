# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging
# than the example.

# Write a function that takes a list of words and returns a
# report of all the words that are longer than 10 characters
# but don't contain a hyphen. If those words are longer than
# 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
  no_hyphen = remove_hyphen(words)
  greater_than_ten = words_greater_than_ten(no_hyphen)
  return "These words are quite long: " + ', '.join(greater_than_ten)

def words_greater_than_ten(words):
  new_words = []
  for word in words:
    word_len = len(word)
    if word_len > 10 and word_len <= 15:
      new_words.append(word)
    elif word_len > 15:
        new_word = word[0:15] + "..."
        new_words.append(new_word)
  return new_words

def remove_hyphen(words):
  new_words = []
  hyphen = '-'
  for word in words:
    if hyphen not in word:
      new_words.append(word)
  return new_words

  
check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
