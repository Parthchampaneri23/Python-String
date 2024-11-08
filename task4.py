# Write a Python program to count and display the vowels of a given text String=”Welcome to python Training

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    vowel_list = []
    for char in text:
        if char in vowels:
            count += 1
            vowel_list.append(char)
    print(f"No. of vowels: {count}")
    print(f"Vowels: {vowel_list}")

text = "Welcome to python Training"
count_vowels(text)
