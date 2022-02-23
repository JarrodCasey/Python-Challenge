# Import Functions
import os
import csv

# State path to collect data from the Resources folder
BudgetData_CSV = os.path.join('Resources','budget_data.csv')

# Open the CSV file
with open(BudgetData_CSV,encoding='utf') as BudgetData_CSVFile:
    # Split the data on commas and state there is a header.
    CSVReader = csv.reader(BudgetData_CSVFile,delimiter = ",")
    header = next(CSVReader)

    # Define the function and have it accept the 'budget_data' as its sole parameter
    def print_BudgetData(budget_data):
        #Assign values to variables
        BudgetDate = str(budget_data[0])
        ProfitLoss = int(budget_data[1])

    # Add variable "TotalMonth" and set to "0"
    TotalMonth = 0
    # Add variable "Total" and set to "0"
    TotalPL = 0
    # Add variable "PrevPeriod" and set to 'Period Start'
    PrevPeriod = 'Period Start'
    # Add variable "TotalChange" and set to "0"
    TotalChange = 0
    # Add variable "GtsIncProf" and set to 'Period Start'
    GrtsIncProf = 'Period Start'
    # Add Variable "GtsIncProfDate" and set to 'Period Start'
    GtsIncProfDate = str()
    # Add variable "GtsDecProf" and set to 'Period Start'
    GrtsDecProf = 'Period Start'
    # Add Variable "GtsDecProfDate" and set to 'Period Start'
    GtsDecProfDate = str()
    # Add Variable "CurrMthChg" and set to "0"
    CurrMthChg = 0
    

    # Start For loop
    for month in CSVReader:
        # Add 1 for every row to count the number of months in a period
        TotalMonth = TotalMonth + 1
        # Add Profit/Loss to get the net total of "Profit/Losses" over the period
        TotalPL += int(month[1])
        # Calculate the changes from month to month over the entire period
        if PrevPeriod == 'Period Start':
            PrevPeriod = int(month[1])
        else:
            TotalChange += int(month[1])-PrevPeriod
            CurrMthChg = int(month[1])-PrevPeriod
            if CurrMthChg >= 0:
                if GrtsIncProf == 'Period Start':
                   GrtsIncProf = CurrMthChg
                   GtsIncProfDate = str(month[0])
                elif CurrMthChg > GrtsIncProf:
                    GrtsIncProf = CurrMthChg
                    GtsIncProfDate = str(month[0])
            if CurrMthChg < 0:
                if GrtsDecProf == 'Period Start':
                   GrtsDecProf = CurrMthChg
                   GtsDecProfDate = str(month[0])
                elif CurrMthChg < GrtsDecProf:
                    GrtsDecProf = CurrMthChg
                    GtsDecProfDate = str(month[0])

            PrevPeriod = int(month[1])

# Calculate the average changes from month to month over the entire period
AveChange = TotalChange/(TotalMonth - 1)
# Format number to 2 decimal places
format_AveChange = "{:.2f}".format(AveChange)

# Print to Terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Month: {TotalMonth}')
print(f'Total: ${TotalPL}')
print(f'Average Change: ${format_AveChange}')
print(f'Greatest Increase in Profits: {GtsIncProfDate} (${GrtsIncProf})')
print(f'Greatest Decrease in Profits: {GtsDecProfDate} (${GrtsDecProf})')
print('----------------------------')

# Create and export results to "FinancialAnalysis.txt" file into the Analysis Folder
save_path = 'Analysis'
file_name = "FinancialAnalysis.txt"

CompleteName = os.path.join(save_path,file_name)
file1 = open(CompleteName,"w")
file1.write('Financial Analysis\n')
file1.write('----------------------------\n')
file1.write(f'Total Month: {TotalMonth}\n')
file1.write(f'Total: ${TotalPL}\n')
file1.write(f'Average Change: ${format_AveChange}\n')
file1.write(f'Greatest Increase in Profits: {GtsIncProfDate} (${GrtsIncProf})\n')
file1.write(f'Greatest Decrease in Profits: {GtsDecProfDate} (${GrtsDecProf})\n')
file1.write('----------------------------')
file1 = open(CompleteName)
file1.close()