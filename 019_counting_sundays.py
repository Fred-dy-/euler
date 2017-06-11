'''
Created on 11 Jun 2017

@author: fgurkov1
'''

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0


def days_between(date1, date2):
    full_years = date2[0] - date1[0]
    days = full_years * 365 + sum([1 for year in range(date1[0], date2[0]) if is_leap(year)])
    days += sum([months[month] for month in range(1, date2[1])])
    if date2[1] > 2 and is_leap(date2[0]):
        days += 1
    days += date2[2] - 1
    return days


def day_of_week(year:int, month:int, day:int) -> int:
    return days_between((1900, 1, 1), (year, month, day)) % 7

def count_sundays(date1, date2):
    count = 0
    for year in range(date1[0], date2[0] + 1):
        for month in range(1, 13):
            if day_of_week(year, month, 1) == 6:
                count += 1
    return count

if __name__ == '__main__':
    print(count_sundays((1901, 1, 1), (2000, 12, 31)))