#Runtime ~0.07s.

number = 2**1000

digit_string_list = list(str(number))
digit_list = map(int, digit_string_list)
print(sum(digit_list))
