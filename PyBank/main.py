#What the assignment is asking for: 
#Total # of months included in data set (add total # of rows except header row)
#Net total of profits/losses over entire period (add all values in index 1 together)
#Changes in profit/losses over entire period, and then average of changes   
#Greatest increase in profits over entire period both date and amount (store the values of the changes from previous step, print the greatest increase)
#Greatest decrease in profits over entire period both date and amount (store values of changes from step 3, print greatest decrease here)

#import the modules
import csv
import os

#define the path to the csv and text file
#if these don't work, please try opening the folder and then running. It works on my end when I do that
budgetfile = os.path.join('Resources', 'budget_data.csv')
outputfile = os.path.join('analysis','budget_analysis.txt')

#create variables to store the greatest increase, greatest decrease, net total of profits, total months, and store the profits/losses of current month to calculate change
month_total = 0
net_total = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""
previous_month_value = 0
change_tracker = 0

#open the file
with open(budgetfile) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header row
    csv_header = next(csvreader)
    #loop
    for row in csvreader:
        #now that the file is open, create and store variables for change between previous and current month as well as running total of net changes month to month
        #adding an if statement so that we don't count the very first month in this calculation
        if previous_month_value != 0:
            net_change = (previous_month_value - int(row[1])) * -1
            change_tracker += net_change
            #check that value to see if it's new record for greatest increase or decrease, and store value as well as date
            if net_change > greatest_increase:
                greatest_increase = net_change
                greatest_increase_month = row[0]
            if net_change < greatest_decrease:
                greatest_decrease = net_change
                greatest_decrease_month = row[0]
        #store new previous month value before moving on to next row
        previous_month_value = int(row[1])
        #add the row to month total, and add the vale in the profit/losses to net_total
        month_total +=1
        net_total += int(row[1])

#once all of the rows have been looped through, calculate the average change and print the values to the text file
#Start by opening the txt output file
with open(outputfile, 'w') as txtfile:
    txtfile.write("Financial Analysis")
    txtfile.write('\n')
    txtfile.write("-----------------------------------")
    txtfile.write('\n')
    txtfile.write(f'Total Months: {month_total}')
    txtfile.write('\n')
    txtfile.write(f'Total: ${net_total}')
    txtfile.write('\n')
    #Need to divide by total months -1 since no change in first month. Thank you username jleverenz on askbcs
    txtfile.write(f'Average Change: ${round(change_tracker/(month_total - 1),2)}')
    txtfile.write('\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    txtfile.write('\n')
    txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')