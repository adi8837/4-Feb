def most_freq_word_len(text):

    words = [word.lower().strip() for word in text.split() if word.isalpha()]
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_frequency = 0
    max_length_word = ""
    for word, count in word_counts.items():
        if count > max_frequency:
            max_frequency = count
            max_length_word = word

    return len(max_length_word)


test_cases = [
    ("write write write all the number from from from 1 to 100", 5),
    ("My name is Aditya. Aditya lives in Delhi NCR. Aditya loves to play football", 4),
    ("hello world how are you doing today", 5),
    ("", 0),
]

for text, expected_output in test_cases:
    result = most_freq_word_len(text)
    print(f"Input: {text}")
    print(f"Output: {result}")
    print(f"Expected: {expected_output}")
    print("-" * 20)

