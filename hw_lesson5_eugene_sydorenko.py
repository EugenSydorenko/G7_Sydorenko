# import re 

sentence = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

# Remove punctuation marks using regular expression
# sentence = re.sub(r'[^\w\s]', '', sentence)
words = sentence.split()
print(words)


# Function to replace vowels in a word with #
def replace_vowels(word):
    vowels = ['а', 'е', 'є', 'и', 'і', 'ї', 'о', 'у', 'ю', 'я']
    for char in word:
        if char.lower() in vowels:
            word = word.replace(char, '#')
    return word


# Replace vowels in each word
modified_words = [replace_vowels(word) for word in words]

# Join the modified words back into a sentence
modified_sentence = ' '.join(modified_words)
print(modified_sentence)
