def is_leap_year(year):
    if year%4==0:
        if year %100==0:
            if year%400:
                return True
            else:
                return  False
        else:
            return True
    else:
        return False

year=int(input("Enter a year"))

if is_leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")