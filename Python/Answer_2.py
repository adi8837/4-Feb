def most_frequent_word_length(text):
  
  words = [word.lower().strip() for word in text.split() if word.isalpha()]

  
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1

  
  max_frequency = 0
  max_length_word = ""
  for word, count in word_counts.items():
    if count > max_frequency:
      max_frequency = count
      max_length_word = word

  
  return len(max_length_word)


text = "My name is Aditya. Aditya lives in Delhi NCR. Aditya loves to play football"
result = most_frequent_word_length(text)
print(f"The length of the most frequent word is: {result}")
