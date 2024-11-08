#Write a Python program to reverse words in a string String = “Deeptech Python Training”

def reverse_words(s):
    words = s.split()  # split the string into a list of words
    reversed_words = words[::-1]  # reverse the list of words
    reversed_string = ' '.join(reversed_words)  # join the reversed words back into a string
    return reversed_string

string = "Deeptech Python Training"
print("Original string:", string)
print("Reversed string:", reverse_words(string))
