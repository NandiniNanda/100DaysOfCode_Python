from collections import Counter

# Function to calculate word frequency
def word_frequency(text):
    words = text.split()
    word_counts = Counter(words)
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_counts

# Take user input for the file name
file_name = input("Enter the file name: ")

try:
    # Read the content of the file
    with open(file_name, 'r') as file:
        file_content = file.read()
        # Calculate word frequency
        result = word_frequency(file_content)
        # Print the result
        for word, frequency in result:
            print(word, frequency)
except FileNotFoundError:
    print("File not found.")

