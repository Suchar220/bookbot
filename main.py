def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

def print_report(filepath, word_count, char_count):
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")

def main():
    filepath = "books/frankenstein.txt"
    
    with open(filepath, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_count = count_characters(file_contents)
    
    print_report(filepath, word_count, char_count)

if __name__ == "__main__":
    main()
