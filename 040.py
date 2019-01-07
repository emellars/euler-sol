#Runtime ~0.11s.

#We want to generate the decimal fraction up to a million digits. This is done by concatenating up until the integer (100000 + ceil(n)) where n is given by 9*1 + 90*2 + 900*3 + 9000*4 + 90000*5 + n*6 = 1000000. Solving gives n = 85185.1(6...).
integer_concatenation = ("".join(str(x) for x in range(185186)))

print(int(integer_concatenation[1]) * int(integer_concatenation[10]) * int(integer_concatenation[100]) * int(integer_concatenation[1000]) * int(integer_concatenation[10000]) * int(integer_concatenation[100000]) * int(integer_concatenation[1000000]))
