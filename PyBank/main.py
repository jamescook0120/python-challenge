import csv 
import os

file = os.path.join('Resources','budget_data.csv')

with open(file) as csvfile: 

    csvreader=csv.reader(csvfile, delimiter=',') 
    header=next(csvreader) 

    months=[]
    profit=[] 
    total=0
    x=0
    monthly_change=0
    month_count=0
    greatest_change=0
    greatest_loss=0
    greatest_month=0
    loss_month=0
    counter1=0
    counter2=0

    
    for row in csvreader:
        month=row[0]
        change_in_money=row[1] 
        months.append(month) 
        profit.append(change_in_money)
    
    month_count = len(months)
  
for counter1 in range (month_count):
    total=total+int(profit[counter1])

for counter2 in range (month_count-1): 
    x=x+(float(profit[counter2+1])-float(profit[counter2]))
    monthly_change=(float(profit[counter2+1])-float(profit[counter2]))
    if monthly_change>greatest_change:
        greatest_change=monthly_change
        greatest_month=counter2
    else:
        greatest_change=greatest_change

    if monthly_change<greatest_loss:
        greatest_loss=monthly_change
        loss_month=counter2
    else:
        greatest_loss=greatest_loss



analysis=f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {month_count}\n\
Total Amount: ${total}\n\
x Change: ${round(x/(month_count-1),2)}\n\
Greatest Increase in Profits: {months[greatest_month+1]} (${int(greatest_change)})\n\
Greatest Decrease in Profits: {months[loss_month+1]} (${int(greatest_loss)})\n'

print(analysis) 
