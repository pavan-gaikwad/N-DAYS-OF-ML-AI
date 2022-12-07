# description: Bag of words

text_data = ["We will use short sentences to illustrate the concepts.",
             "Once we get the concept of bag of words, we can move on."]

# Create a set of unique words from the text data
vocabulary = set()
for text in text_data:
    words = text.split()
    vocabulary.update(words)

# Create the bag of words representation of the text data
bag_of_words = []
for text in text_data:
    words = text.split()
    count = [words.count(word) for word in vocabulary]
    bag_of_words.append(count)

# Print the bag of words representation of the text data
print("Vocabulary:", vocabulary)
print("Bag of words:", bag_of_words)
