def count_words(text):
    words = text.split()
    return len(words)  # Return word count

def count_letters(text):
    letters = [char for char in text if char.isalpha()]  # Count only letters
    return len(letters)  # Return letter count

def main():
    with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)  
    letter_count = count_letters(file_contents)  # Call count_letters properly
    
    
    print(f"Letter count: {letter_count}")

main()