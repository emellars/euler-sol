#Runtime ~0.076s.

#Input "triplet" is a collection of three numbers [a, b, c]. The output of the function is this number in words. (E.g. [1,1,2] returns onehundredandtwelve).
def english_number(triplet):
    while triplet[0] == 0:
        if len(triplet) == 1: return "" #Returns a string of length 0 if [0, 0, 0] is the input.
        triplet = triplet[1:] #Converts [0, x] to [x].
    #Single digit numbers.
    if len(triplet) == 1:
        if triplet[0] == 1: return "one"
        elif triplet[0] == 2: return "two"
        elif triplet[0] == 3: return "three"
        elif triplet[0] == 4: return "four"
        elif triplet[0] == 5: return "five"
        elif triplet[0] == 6: return "six"
        elif triplet[0] == 7: return "seven"
        elif triplet[0] == 8: return "eight"
        else: return "nine"
    #Double digit numbers.
    if len(triplet) == 2:
        if triplet[0] == 1:
            if triplet[1] == 0: return "ten"
            if triplet[1] == 1: return "eleven"
            if triplet[1] == 2: return "twelve"
            if triplet[1] == 3: return "thirteen"
            if triplet[1] == 4: return "fourteen"
            if triplet[1] == 5: return "fifteen"
            if triplet[1] == 6: return "sixteen"
            if triplet[1] == 7: return "seventeen"
            if triplet[1] == 8: return "eighteen"
            if triplet[1] == 9: return "nineteen"
        elif triplet[0] == 2:
            return "twenty" + english_number(triplet[1:])
        elif triplet[0] == 3:
            return "thirty" + english_number(triplet[1:])
        elif triplet[0] == 4:
            return "forty" + english_number(triplet[1:])
        elif triplet[0] == 5:
            return "fifty" + english_number(triplet[1:])
        elif triplet[0] == 6:
            return "sixty" + english_number(triplet[1:])
        elif triplet[0] == 7:
            return "seventy" + english_number(triplet[1:])
        elif triplet[0] == 8:
            return "eighty" + english_number(triplet[1:])
        else:
            return "ninety" + english_number(triplet[1:])
    #Triple digit numbers.
    if len(triplet) == 3:
        if triplet[1] == 0 and triplet[2] == 0:
            return english_number(triplet[:1]) + "hundred"
        x = "hundredand"
        if triplet[0] == 1:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 2:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 3:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 4:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 5:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 6:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 7:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        elif triplet[0] == 8:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])
        else:
            return english_number(triplet[:1]) + x + english_number(triplet[1:])

length = len("onethousand") #Count the only four digit number manually.
#Iterate over numbers from 1 to 999 and cumulatively add up the lengths.
for i in range(10):
    for j in range(10):
        for k in range(10):
            length += len(english_number([i, j, k]))

print(length)
