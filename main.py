def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    count_of_words = word_count(file_contents)
    count_of_charters = character_count(file_contents)

    print_report(path_to_file, count_of_words, count_of_charters)

def word_count(s):
    word_list = s.split()
    word_count = len(word_list)
    
    return word_count

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
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    sorted_characters = sort_dictionary(characters)
    
    for letter in sorted_characters:
        if not letter.isalpha():
            continue
        print(f"The '{letter}' character was found {sorted_characters[letter]} times")

    print("--- End report ---")



main()