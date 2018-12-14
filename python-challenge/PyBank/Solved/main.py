# Modules
import os
import csv


# Set path for file
#csvpath = "C:\\Users\\C00979\\DataViz-Lesson-Plans\\01-Lesson-Plans\\03-Python\\2\\Activities\\08-Stu_ReadNetFlix\\Resources\\netflix_ratings.csv"
csvpath = os.path.join("..", "Resources", "budget_data.csv")

total = 0 
num_months = 0 
greatest_increase = 0
greatest_decrease = 0 
greatest_month = str()
lowest_month = str()
previous = 0
change = 0 
change_list = []
total_change = 0
average_change = 0 

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
            #print(row[0])
            total = total + float(row[1])
            num_months = num_months + 1
            change = float(row[1]) - float(previous)
            change_list.append(change)
            if float(change) > float(greatest_increase):
                greatest_increase = change
                greatest_month = row[0]
            if float(change) < float(greatest_decrease):
                greatest_decrease = change
                lowest_month = row[0]    
            previous = float(row[1])
    change_list.pop(0)
    average_change = sum(change_list)/(num_months-1)
    
print(f"Total Months: {num_months}")
print(f"Total: ${round(total,2)}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease: {lowest_month} (${greatest_decrease})")

