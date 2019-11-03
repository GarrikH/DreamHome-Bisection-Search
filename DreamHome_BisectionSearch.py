#!/usr/bin/env python
# coding: utf-8

import numpy as np
import math

print('\nThis program will calculate the rate you need to save at to afford your dream home within the next 36 months.\n\n')

starting_salary = float(input('Enter the starting salary: '))

raise_percent = 0.07
r = 0.04
percent_down = float(input('Enter the percent you will put down in decimal format: '))
house_cost = float(input('Enter the price of the house: '))

min_saved = house_cost * percent_down
save_high = min_saved + 100
amt_saved = 0.0
search_high = 10000
search_low = 0
searches = 0
max_searches = math.floor(np.log2(search_high)) + 1
while(not(min_saved <= amt_saved <= save_high) and searches != max_searches):
    guess = math.floor(((search_high + search_low) / 2))
    month = 0
    target_savings = 0.0
    percent_save = float(guess / 10000)
    annual_salary = starting_salary
    while(month < 36):
        target_savings += ((annual_salary/12) * percent_save)
        target_savings *= (1 + (r/12))
        month += 1
        if(month % 6 == 0):
            annual_salary *= (1 + raise_percent)
            
    amt_saved = target_savings
    if(amt_saved < min_saved):
        search_low = guess
    elif(amt_saved > save_high):
        search_high = guess
    searches += 1
        

if(searches == max_searches):
    print('\n\nIt is not possible to pay the down payment in three years, sorry.')
else:
    percent_save *= 100
    print('\n\nBest savings rate: {0:.2f}%'.format(percent_save))
    print('Steps in bisection search:', searches)

