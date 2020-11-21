#import file

import os
import csv

#path to the csvfile
csvpath = os.path.join("Resources","budget_data.csv")

#initializing the variables 
total_months = 0
total_revenue =0
changes =[]
date_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0


# Open the CSV
with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    row = next(csvreader)

# calculating the total number of months and total revenue
    previous_profit = int(row[1])
    total_months = total_months + 1
    total_revenue = total_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]
    
  # calculate the change in profit/loss
     total_profit_loss += int(row[1])
    diff_ProfitLoss = int(row[1]) - prev_profit_loss
    
 #To calculate avg.
        total_changeinPL += diff_ProfitLoss 
    
 for row in csvreader:
 
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Calculate change from this month to previous months
        change = int(row[1]) - previous_profit
        changes.append(change)
        previous_profit = int(row[1])
        date_count.append(row[0])
        

 # The greatest increase in profits (date and amount) over the entire period
        if diff_ProfitLoss > greatest_inc:
            greatest_inc = diff_ProfitLoss
            greatest_inc_month = row[0] 

# The greatest decrease in losses (date and amount) over the entire period
        if diff_ProfitLoss < greatest_dec:
            greatest_dec = diff_ProfitLoss
            greatest_dec_month = row[0]
            
# The average of the changes in "Profit/Losses" over the entire period.        
avg_ProfitLoss = total_changeinPL / (total_months - 1)
    
# Print the analysis to terminal
print("Financial Analysis")
print("----------------------------")        
print("Total Months: " + str(total_months))
print("Total: $" + str(total_profit_loss))
print("Average Change: $" + str(format(avg_ProfitLoss, '.2f')))
print("Greatest Increase in Profits: " + greatest_inc_datemonth + " ($" + str(greatest_inc_amount) + ")")
print("Greatest Decrease in Profits: " + greatest_dec_datemonth + " ($" + str(greatest_dec_amount) + ")")

# Write to text file Analysis_PyBank.txt
f = open("Analysis_PyBank.txt", "w")
f.write("Financial Analysis\n")
f.write("----------------------------\n")        
f.write("Total Months: " + str(total_months) + "\n")
f.write("Total: $" + str(total_profit_loss) + "\n")
f.write("Average Change: $" + str(format(avg_ProfitLoss, '.2f')) + "\n")
f.write("Greatest Increase in Profits: " + greatest_inc_datemonth + " ($" + str(greatest_inc_amount) + ")\n")
f.write("Greatest Decrease in Profits: " + greatest_dec_datemonth + " ($" + str(greatest_dec_amount) + ")\n")
f.close()        