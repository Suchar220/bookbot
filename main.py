def count_words(text):
    words = text.split()
    return len(words)  # Return word count

def count_letters(text):
    letters = [char for char in text if char.isalpha()]  # Count only letters
    return len(letters)  # Return letter count

def count_characters(text):
    text = text.lower()  # Convert text to lowercase
    char_count = {}  # Dictionary to store counts
    
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count  # Return dictionary of character counts

def main():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)  
    letter_count = count_letters(file_contents)  
    char_count = count_characters(file_contents)  # Call new function
    
    print(f"Word count: {word_count}")
    print(f"Letter count: {letter_count}")
    print("Character count:", char_count)  # Print dictionary

main()
