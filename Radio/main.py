import pygame


def is_year_leap(year):
    if year >= 0:
        return (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
    else:
        return False

def days_in_month(year, month):
    month_lengths_leap = [31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    month_lengths = [31, 30, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    if is_year_leap(year) and month == 2:
        return month_lengths_leap
    elif month <= 0 or month >= 13:
        return None
    else:
       return month_lengths

def day_of_year(year, month, day):
    if year < 0:
        return None
    else:
        aux = 0
        for y in days_in_month(year, month):
            aux = aux + y
        return aux

print(day_of_year(2000, 12, 31))
