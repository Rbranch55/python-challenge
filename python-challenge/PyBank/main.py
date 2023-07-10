# Import 
import os
import csv
import datetime

print("Financial Analysis")
print("------------------")

csvpath = os.path.join('/Users/t/Downloads/python-challenge/PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

## The total number of months included in the dataset
from datetime import datetime

dates = ['10-Jan', '10-Feb', '10-Mar', '10-Apr', '10-May', '10-Jun', '10-Jul', '10-Aug', '10-Sep', '10-Oct', '10-Nov', '10-Dec',
'11-Jan', '11-Feb', '11-Mar', '11-Apr', '11-May', '11-Jun', '11-Jul', '11-Aug', '11-Sep', '11-Oct', '11-Nov', '11-Dec',
'12-Jan', '12-Feb', '12-Mar', '12-Apr', '12-May', '12-Jun', '12-Jul', '12-Aug', '12-Sep', '12-Oct', '12-Nov', '12-Dec',
'13-Jan', '13-Feb', '13-Mar', '13-Apr', '13-May', '13-Jun', '13-Jul', '13-Aug', '13-Sep', '13-Oct', '13-Nov', '13-Dec',
'14-Jan', '14-Feb', '14-Mar', '14-Apr', '14-May', '14-Jun', '14-Jul', '14-Aug', '14-Sep', '14-Oct', '14-Nov', '14-Dec',
'15-Jan', '15-Feb', '15-Mar', '15-Apr', '15-May', '15-Jun', '15-Jul', '15-Aug', '15-Sep', '15-Oct', '15-Nov', '15-Dec',
'16-Jan', '16-Feb', '16-Mar', '16-Apr', '16-May', '16-Jun', '16-Jul', '16-Aug', '16-Sep', '16-Oct', '16-Nov', '16-Dec',
'17-Jan', '17-Feb']

formatted_dates = [datetime.strptime(date, "%y-%b") for date in dates]

# Convert each date string to a unique month using a set comprehension 
months = {date.split("-")[1] 
    for date in dates} 
# Calculate the total number of unique months
total_months = len(dates)
# Print the result 
print("Total Months:", total_months)

## The net total amount of "Profit/Losses" over the entire period
data = [1088983, -354534, 276622, -728133, 852993, 563721, -535208, 632349, -173744, 950741, -785750, -1194133, -589576, -883921, 443564, 837887, 1081472, 464033, -1066544, 323846, -806551, 487053, 1128811, 791398, 739367, -197825, 666016, 589771, 489290, -471439, 120417, 175347, 855449, 605195, -235220, 347138, 298510, 163254, 1141840, 542630, 99841, 752765, -252949, 914424, 679524, 514377, 462102, 159782, 878810, -946748, 340335, 292032, 502266, 265852, 851017, -549615, 290162, 755391, 1073202, 313000, 241132, 1036589, 853904, -388932, 982952, 537759, 547784, -496214, 854181, 934719, -288531, -184383, 659541, -1149123, 355882, 662284, 518681, -748256, -910775, 951227, 898241, -729004, -112209, 516313, 607208, 382539]

net_total = sum(data)
formatted_total = f"Total: ${net_total}"
print(formatted_total)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

changes = [data[i+1] - data[i] for i in range(len(data)-1)]

# Calculate the average of the changes
average_change = sum(changes) / len(changes)

# Print the results
rounded_number = round(average_change, 2)
print("Average Change:", rounded_number)

## The greatest increase in profits (date and amount) over the entire period
changes = []
for i in range(1, len(data)):
    change = data[i] - data[i-1]
    changes.append(change)
import datetime
max_increase = max(changes)
max_increase_index = changes.index(max_increase)
max_increase_date = dates[max_increase_index + 1]
date_str = max_increase_date
# Parse the input date
date_obj = datetime.datetime.strptime(date_str, '%y-%b')

# Convert the date to the desired format 'month abbreviated-YY'
new_date_str = date_obj.strftime('%b-%y')

# Print the results
formatted_increase = f"Greatest Increase in profits: {new_date_str} ${max_increase}"
print(formatted_increase)

## The greatest decrease in profits (date and amount) over the entire period
changes = []
for i in range(1, len(data)):
    change = data[i] - data[i-1]
    changes.append(change)
import datetime
max_decrease = min(changes)
max_decrease_index = changes.index(max_decrease)
max_decrease_date = dates[max_decrease_index + 1]
date_str2 = max_decrease_date
# Parse the input date
date_obj = datetime.datetime.strptime(date_str2, '%y-%b')

# Convert the date to the desired format 'month abbreviated-YY'
new_date_str = date_obj.strftime('%b-%y')

# Print the results
formatted_decrease = f"Greatest Decrease in profits: {new_date_str} ${max_decrease}"
print(formatted_decrease)

# Open the file in write mode
file_name = "Fianancial Analysis.txt"
file = open(file_name, 'w')

# Write content to the file
content = "Financial Analysis ------------------ Total Months: 86 Total: $22564198 Average Change: -8311.11 Greatest Increase in profits: Aug-16 $1862002 Greatest Decrease in profits: Feb-14 $-1825558"

file.write(content)

# Close the file
file.close()