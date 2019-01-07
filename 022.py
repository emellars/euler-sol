#Runtime ~0.08s.

#Returns position of letter in alphabet.
def alpha_position(letter):
    return ord(letter.title()) - 64

#Convert alphabet value to a number. (A = 1, B = 2, ..., Z = 26.)
def alpha_value(str):
    sum = 0
    for element in str:
        sum += alpha_position(element)
    return sum

with open("022.txt", "r") as name_data:
    name_list = name_data.read()

names = name_list.split(",")
names = sorted([x.replace("\"", "") for x in names], key = str.lower)

#Convert all names to their corresponding numeric value.
name_values = list(map(alpha_value, names))

#Rank names.
name_scores = [(x + 1)*name_values[x] for x in range(len(name_values))]

print(sum(name_scores))
