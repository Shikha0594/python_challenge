import os
import csv
csvpath = os.path.join('.','Resources', 'budget_data.csv')
with open (csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csv_reader)
    total_months = 0
    total_pl = 0
    value = 0
    change = 0
    Dates = []
    profits = []

    first_row = next(csv_reader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])


    for row in csv_reader:
        Dates.append(row[0])

        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        total_months += 1
        total_pl = total_pl + int(row[1])

        greatest_increase = max(profits)
        greatest_index = profits.index(greatest_increase)
        greatest_Date = Dates[greatest_index]

        greatest_decrease = min(profits)
        worst_index = profits.index(greatest_decrease)
        worst_Date = Dates[worst_index]

        avg_change = sum(profits)/len(profits)



  

print("Financial Analysis")
print("------------------------------------------------")
print( f"Total months: {str(total_months)}")
print( f"Total: ${str(total_pl)} ")
print(f"Average change: ${str(round(avg_change,2))} ")
print( f"Greatest Increase in profits : {greatest_Date} (${str(greatest_increase)}) ")
print( f" Greatest Decrease in profits : {worst_Date} (${str(greatest_decrease)})")

output = open("output.text", "w")

line1 = "Financial Analysis"
line2 = "---------------------------------------------------"
line3 = str( f"Total months: {str(total_months)}")
line4 = str( f"Total: {str(total_pl)}")
line5 = str( f"Average change: ${str(round(avg_change,2))}")
line6 = str( f"Greatest Increase in profits : {greatest_Date} (${str(greatest_increase)})")
line7 = str( f"Greatest Decrease in profits : {worst_Date} (${str(greatest_decrease)})")
output.write(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}\n")




