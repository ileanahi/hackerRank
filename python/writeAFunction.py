def is_leap(year):
    leap = False

    # Write your logic here
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
year = int(raw_input())
print is_leap(year)
