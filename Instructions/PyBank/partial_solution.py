import os
import csv

path = os.path.join("Resources", "budget_data.csv")

sum_profits = 0
count = 0
with open(path, "r") as file:
    print("file: ", file)
    reader = csv.DictReader(file)
    print("reader: ", reader)
    
    for row in reader:
        print(50 * "=")
        print("type(row): ", type(row))
        print("row: ", row)
        row_dict = dict(row)
        print("row_dict: ", row_dict)
        profit = row_dict["Profit/Losses"]
        print("profit: ", profit)
        print("type(profit): ", type(profit))
        profit_float = float(profit)
        print("profit_float: ", profit_float)
        sum_profits += profit_float
        print("sum_profits: ", sum_profits)
        count += 1
        print("count: ", count)
        
        print("This prints every time through the loops")
    
    print("Here the file is still avialible.")

print("the file is closed")
print(50 * "=")
print("sum_profits: ", sum_profits)
avg_profits = sum_profits / count
print("avg_profits: ", avg_profits)



        
    