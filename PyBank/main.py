#PyBank Homework
import os
import csv
from collections import defaultdict

with open('/Users/ZGS/Documents/Data_Bootcamp/Python_homework/python-challenge/PyBank/budget_data_1.csv', 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    budget_data = list(csv_reader)
    
    #list of months
    months = [i[0] for i in budget_data]
    
    #list of revenue
    monthly_revenue = budget_data
    monthly_revenue = [eval(x[1]) for x in monthly_revenue]
    
    total_revenue = (sum(monthly_revenue[0:]))
    print("Total Revenue: $", total_revenue)
    print ("Total Months:", len(budget_data))
    total_change = 0
    
    for index, row in enumerate(monthly_revenue, 1):
        #calculate average change in revenue
        current_change = [x - y for x, y in zip(monthly_revenue[1:], monthly_revenue)]
        total_change = sum(current_change)
        average_change = int(total_change / (len(budget_data) -1))
        print("Average Monthly Change: $", average_change)
        
        #calculate largest increase in revenue between months
        max_increase = max(current_change)
        print("Largest Increase In Revenue:", months[date_increase],"$", max_increase)
        date_increase = current_change.index(max_increase)+1
        
        #Calculate largest decrease in revenue between months
        max_decrease = min(current_change)
        print("Largest Decrease In Revenue:", months[date_decrease],"$", max_decrease)
        date_decrease = current_change.index(max_decrease)+1
        break
