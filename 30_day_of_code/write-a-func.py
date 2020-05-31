# python3

# Input format: read y, the year that needs to be checked

# output: function must return bool values (True/False)

# constraints: 1900 <= y <= 10**5


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


year = int(input())
print(is_leap(year))
