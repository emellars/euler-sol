#Runtime ~0.92s.

def number_to_list(n):
    n = str(n)
    return map(int, n)

def sum_fifth_powers(l):
    result = 0
    for n in l:
        result += n**5
    return result

#Note that (9**5)*6 < 999999 which is the worst case for six digits, hence a tentative lower bound on the maximum number to be checked is 999999. The lower bound is improved by considering the lowest digit x such that x**5 + (9**5)*5 > x99999, which occurs for x = 3. Hence we need only check numbers up to 299999.
fifth_power_sums = [n for n in range(2, 300000) if n == sum_fifth_powers(number_to_list(n))]
print(sum(fifth_power_sums))
