# Your code here

# Read the file, get string
# Create a function for word count, pass the string for evaluation
# lower case the string
# Gather the ignorable symbols
# Cut the ignorable symbols out of the string
# Split the string into a list of words
# Find while its a list - the max length of the string
# Create a dict
# iterate through the list of words
# If the word is not inside the dictionary, crea a key for the word and assign value of 1
# If it exists, increase the value

# sort by the count in descending order, then by the key alphabetically

# loop through words
# do something to add the right amount of spaces after each word
# subtract length of word from the max value, multiply that number by "
# make sure to account for the 2 spaces for the longest word

# print out the # symbols based on value (x * the count)


with open("robin.txt") as f:
    words = f.read()

punct = ['"', ':', ';', ',', '.', '-', '+', '=', '/',
         '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&']
for char in punct:
    words = words.replace(char, '')

word_list = words.split()

word_count = {}

for word in word_list:
    if word.lower() in word_count:
        word_count[word.lower()] += 1
    else:
        word_count[word.lower()] = 1

sorted_word_list = sorted(word_count, key=word_count.get, reverse=True)

for i in range(len(sorted_word_list)):
    bar = '#' * word_count[sorted_word_list[i]]
    print(f'{sorted_word_list[i]:15} {bar}')
