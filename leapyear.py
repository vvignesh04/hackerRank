def is_leap(year):
    leap = False
    if year%400==0 or year%4==0 and not year%100==0:
        return not leap
    else:
        return leap
    

year = int(input())
print(is_leap(year))
