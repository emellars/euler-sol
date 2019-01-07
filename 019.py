#Runtime ~0.07s.

#Determines if the year "n" is a leap year.
def is_leap_year(n):
    if n % 400 == 0: return True
    elif n % 100 == 0: return False
    elif n % 4 == 0: return True
    else: return False

#Determines if a month started with Sunday.
def month_starting_sunday(days):
    if days % 7 == 2: return 1
    else: return 0

#1 Jan 1900 begins on a Monday and the year has 365 days. Since 365 % 7 = 1, Jan 1901 must begin on a Tuesday.
#1901 % 7 = 4 corresponds to Tuesday. So we may take the current year (adjusted for leap years) and add the number of days in each month and divide by 7. If the remainder is 2, that month began with a Sunday.
year=1901
remaining_months = [31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cumulative_leap_years = 0
cumulative_sundays = 0
while year < 2001:
    if is_leap_year(year - 1): cumulative_leap_years += 1
    adjusted_year = year + cumulative_leap_years #If the preceding year was a leap year, then, since 365 % 7 = 2, the January of that year starts on a day advanced one more than would be expected if all years were 365 days long.

    #Determine if each month of the year started with a Monday.
    #January.
    if adjusted_year % 7 == 2:
        cumulative_sundays += 1

    #February.
    if is_leap_year(year): number_of_days = 31 + 29
    else: number_of_days = 31 + 28
    cumulative_sundays += month_starting_sunday(adjusted_year + number_of_days)

    #Remaining months in year.
    for days in remaining_months:
        number_of_days += days
        cumulative_sundays += month_starting_sunday(adjusted_year + number_of_days)

    year += 1

print(cumulative_sundays)
