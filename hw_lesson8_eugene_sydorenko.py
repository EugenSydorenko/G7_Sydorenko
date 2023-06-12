def show_file_content(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")


# Reading file content and printing it to console:
show_file_content("file.txt")


def save_string_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)


# Writing content in file
file_name = 'file.txt'  # The desired file name
content = 'This is the content to be saved in the file.'

save_string_to_file(file_name, content)


def replace_string_in_file(file_name, search_string, replacement_string):
    with open(file_name, 'r') as file:
        content = file.read()

    new_content = content.replace(search_string, replacement_string)

    with open(file_name, 'w') as file:
        file.write(new_content)


# String replacement usage
file_name = 'file.txt'  # Specify the file name
search_string = 'old string'  # Specify the string to search for
replacement_string = 'new string'  # Specify the replacement string

replace_string_in_file(file_name, search_string, replacement_string)


def count_words_in_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    word_count = len(content.split())
    print(f'Total words in the file: {word_count}')


# Usage
file_name = 'file.txt'  # Specify the file name

count_words_in_file(file_name)


def search_and_move_sentences(log_file, keyword, output_file):
    matched_sentences = []

    with open(log_file, 'r') as file:
        for line in file:
            if keyword in line:
                matched_sentences.append(line)

    if matched_sentences:
        with open(output_file, 'w') as output:
            for sentence in matched_sentences:
                output.write(sentence)
                print(sentence.strip())  # Print the sentence

        print(f"Matched sentences have been moved to '{output_file}'.")
    else:
        print(f"No sentences containing the keyword '{keyword}' were found in the log file.")


# Usage
log_file = 'log.txt'  # Specify the log file name
keyword = 'word'  # Specify the keyword to search for
output_file = 'file.txt'  # Specify the output file name

search_and_move_sentences(log_file, keyword, output_file)


def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())


# Usage
source_file = 'log.txt'  # Specify the source file name
destination_file = 'file.txt'  # Specify the destination file name

copy_file(source_file, destination_file)
