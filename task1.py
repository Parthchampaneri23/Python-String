#Write a Python program to count the occurrences of each word in a given sentence string = “To change the overall look of your document. To change the look available in the gallery”

def count_word_occurrences(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Create a dictionary to store the word counts
    word_counts = {}

    # Iterate over each word in the sentence
    for word in words:
        # Remove punctuation from the word
        word = word.strip('.,;:!?"\'').lower()

        # If the word is already in the dictionary, increment its count
        if word in word_counts:
            word_counts[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_counts[word] = 1

    # Return the dictionary of word counts
    return word_counts

# Test the function with the given sentence
sentence = "To change the overall look of your document. To change the look available in the gallery"
word_counts = count_word_occurrences(sentence)

# Print the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")
