# python3

# Input format: read y, the year that needs to be checked

# output: function must return bool values (True/False)

# constraints: 1900 <= y <= 10**5


def is_leap(year):
    leap = False

    # Write your logic here

    if(year%100 != 0 and year%400 != 0):
        return leap

    else:

        leap = True
        return leap

year = int(input())
print(is_leap(year))
