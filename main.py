import sys
from stats import word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_file = sys.argv[1]

    with open(path_to_file) as f:
        file_contents = f.read()
    
    count_of_words = word_count(file_contents)
    count_of_charters = character_count(file_contents)

    print_report(path_to_file, count_of_words, count_of_charters)

def character_count(s):
    lower_case_s = s.lower()

    letter_count = {}

    for c in lower_case_s:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1

    return letter_count

def sort_dictionary(d):
    sorted_by_values_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_values_desc

def print_report(file_name, word_count, characters):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    sorted_characters = sort_dictionary(characters)
    
    for letter in sorted_characters:
        if not letter.isalpha():
            continue
        print(f"{letter}: {sorted_characters[letter]}")

    print("============= END ===============")



main()