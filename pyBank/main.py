import os
import csv

#from tomlkit import key_value

#set path for the file
csvpath = './Resource/budget_data.csv'

#Initiate dictionaries to store the values for each column
column1_values = {}
column2_values = {}

#initiate variables
tot_profit = 0
tot_loss = 0
tot_months = 0
differences = []
pnl_per_month = []
months = []
greatest_increase = float('-inf')
greatest_increase_month = ""
greatest_decrease = float('inf')
greatest_decrease_month = ""

#open the csv file and read
with open(csvpath,'r') as budgetfile:
    csvReader = csv.reader(budgetfile)
    header = next(csvReader)
    #print(list(csvReader))


    #to count number of months
    for row in csvReader:
        tot_months += 1
        #to calculate the total profit or loss
        value = float(row[1])
        if value >0:
            tot_profit += value
        else:
            tot_loss += value 

        #to read the profit or loss data per month into a list
        month = row[0]
        pnl_per_month.append(float(row[1]))
        months.append(month)    
    
net_profit_loss = tot_profit + tot_loss

        
#to calculate the difference month on month
for i in range(1,len(pnl_per_month)):
    difference = pnl_per_month[i] - pnl_per_month[i-1]
    differences.append(difference)

#calculate the average
    average_difference = sum(differences)/len(differences)

#find the greatest increase and greatest decrease and corresponding months
    if difference > greatest_increase:
        greatest_increase = difference
        greatest_increase_month = months[i]
    if difference < greatest_decrease:
        greatest_decrease = difference
        greatest_decrease_month = months[i]



output = 'Financial Analysis\n'
output += '------------------------------------------\n'
output += f"Total Months: {tot_months}\n"
output += f"Total: ${net_profit_loss}\n"
output += f"Average Change: {average_difference:.2f}\n"
output += f"Greatest Increase in Profits: {greatest_increase_month} ${greatest_increase}\n"
output += f"Greatest Decrease in Profits: {greatest_decrease_month} ${greatest_decrease}\n"

print(output)

#to write the results to a text file

with open('./Analysis/results.txt','w') as Resultsfile:
    Resultsfile.write(output)