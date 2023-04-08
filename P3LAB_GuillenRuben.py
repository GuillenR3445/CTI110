is_leap_year = False
   
input_year = int(input())

if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    print(input_year, "- leap year")
else:
    print(input_year, "- not a leap year")