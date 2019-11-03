

import csv
import os

# input and output files
inputs = "C:/Users/edenh/OneDrive/Desktop/Python Final/budget_data.csv"
outputs = "C:/Users/edenh/OneDrive/Desktop/Python Final/Eden.txt"
#Creat variables and assign zero 
No_months = 0
total_amount = 0
intial = 0
maxIncrease = 0
maxDecrease = 0
#create a list 
monthly_change = [] 
# Read the csv and convert it into a list of list
with open(inputs) as data:
    reader = csv.DictReader(data)
    
    for row in reader:
        # Track the total
        No_months = No_months + 1
        total_amount = total_amount + int   (row['Profit/Losses'])

        if No_months > 1 :
            change=int(row['Profit/Losses'])-intial
            monthly_change+=[change] #adding items to the list
        
            if change > maxIncrease :
                maxIncrease = change
                maxIncreaseMonth = row['Date']
                
            if change < maxDecrease :
                maxDecrease = change
                maxDecreaseMonth = row['Date']                
            
        intial=int(row['Profit/Losses'])
        
average = round(sum(monthly_change)/(len(monthly_change)+0.0),2)

result=('Total No of months:{}'.format(str(No_months))+'\n'
'The net profit:{}'.format(str(total_amount))+'\n'
'The avarage change in profit/Losses within months:{}'.format(str(average))+'\n'
'The greatest increase in profits (year and amount) : ' + maxIncreaseMonth + ' $'+str(maxIncrease) +'\n'
'The greatest decrease in losses (date and amount) : ' + maxDecreaseMonth + ' $'+str(maxDecrease) +'\n')

with open(outputs,'w') as outputfile:
    outputfile.write(result)
    print(result)
