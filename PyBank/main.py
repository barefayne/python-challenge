import os
import csv

# csv file path
budget_csv = "Resources/budget_data.csv"

# List/ variables
m_count = 1
total = 0
avg_change = 0
max_increase = 0
max_decrease = 0
new_c= []
current_value = 0
# the empty string will hold the month and the 0 will hold the value
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# open csv
with open(budget_csv, 'r', encoding= 'utf-8') as budget_file:
    budget_rows = csv.reader(budget_file, delimiter=',')

    headers = next(budget_rows)
    first_row = next(budget_rows)
    current_value = int(first_row[1])
    total = total + current_value

# Read each row 
    for row in budget_rows:

      # The total number of months included in the dataset
        m_count +=1

       # The net total amount of "Profit/Losses" over the entire period 
        #total += int(row[1])
        total = total + int(row[1])

# The changes in "Profit/Losses" over the entire period, ...
        change = int(row[1]) - current_value
        new_c.append(change)
        current_value = int(row[1])

# The greatest increase in profits (date and amount) over the entire period

        if change > greatest_increase[1]:
            greatest_increase[1] = change
            greatest_increase[0] = row[0]
    
# The greatest decrease in profits (date and amount) over the entire period

        if change < greatest_decrease[1]:
            greatest_decrease[1] = change
            greatest_decrease[0] = row[0]

# ...and then the average of those changes

avg_change = round((sum(new_c)/ len(new_c)),2)
        
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {m_count}")
print(f"Total: ${total}")
print(f"Total: ${avg_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")

# Output path
output_path = "analysis/results.txt"

# Open the output file
with open(output_path, 'w') as text_file:

  # Write rows
  text_file.write(f"Financial Analysis\n")
  text_file.write(f"----------------------------\n")
  text_file.write(f"Total Months: {m_count}\n")
  text_file.write(f"Total: ${total}\n")
  text_file.write(f"Total: ${avg_change}\n")
  text_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}\n")
  text_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}\n")




    