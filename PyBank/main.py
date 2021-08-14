#Write a Python script that analyzes the PyBank Record to calculate each of the following:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

# Define PyBank's variables
months = []
loss_changes = []

count_months = 0
loss_net = 0
previous_loss = 0
current_loss = 0
profit_loss_change = 0

#pulling needed csv file 

budget_data_csv_path = os.path.join("Resources", "budget_data.csv")
with open(budget_data_csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#looping through needed data for calculations
    for row in csv_reader:

        count_months += 1

        current_loss = int(row[1])
        loss_net += current_loss

        if (count_months == 1):
           
            previous_loss = current_loss
            continue

        else:
            profit_loss_change = current_loss - previous_loss
            months.append(row[0])
            loss_changes.append(profit_loss_change)
            previous_loss = current_loss

#calculations
    sum_profit_loss = sum(loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)
    highest_change = max(loss_changes)
    lowest_change = min(loss_changes)
    highest_month_index = loss_changes.index(highest_change)
    lowest_month_index = loss_changes.index(lowest_change)
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

#Print to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${loss_net}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")

#output to .txt file in analysis folder 

FinalAnalysis = r"C:\Users\Antwon\Desktop\DataHomework\Python-Challenge\Python-Challenge\PyBank\Analysis\FinalAnalysis.txt"
with open (FinalAnalysis, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months:  {count_months}\n") 
    output.write(f"Total:  ${loss_net}\n")
    output.write(f"Average Change:  ${average_profit_loss}\n")
    output.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    output.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")