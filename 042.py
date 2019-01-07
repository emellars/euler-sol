#Runtime ~0.075s.

#Returns position of letter in alphabet.
def alpha_position(letter):
    return ord(letter.title()) - 64

#Convert alphabet value to a number. (A = 1, B = 2, ..., Z = 26.)
def alpha_value(str):
    sum = 0
    for element in str:
        sum += alpha_position(element)
    return sum

with open("042.txt", "r") as word_data:
    word_list = word_data.read()

words = word_list.split(",")
words = [word.replace("\"", "") for word in words]

max_characters = max(map(len, words))

triangle_numbers=[]
n, triangle_number = 1, 1
#Generate all possible triangle numbers that could, in principle, be generated from the word list.
while triangle_number < 26*max_characters:
    triangle_numbers.append(triangle_number)
    n += 1
    triangle_number = int((1/2)*n*(n+1))

triangle_word_values = [alpha_value(word) for word in words if alpha_value(word) in triangle_numbers]
print(len(triangle_word_values))
