sentence = input("Enter a sentence: ")

num_chars = len(sentence)
num_words = len(sentence.split())

vowels = "aeiouAEIOU"
num_vowels = 0
for char in sentence:
    if char in vowels:
        num_vowels = num_vowels + 1

num_spaces = 0
for char in sentence:
    if char == " ":
        num_spaces = num_spaces + 1

num_digits = 0
for char in sentence:
    if char.isdigit():
        num_digits = num_digits + 1

result = (num_chars, num_words, num_vowels, num_spaces, num_digits)

print(result)