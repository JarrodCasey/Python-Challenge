# Import Functions
import os
import csv

# State path to collect data from the Resources folder
ElectionData_CSV = os.path.join('Resources','election_data.csv')

# Open the CSV file
with open(ElectionData_CSV,encoding='utf') as ElectionData_CSVFile:
    # Split the data on commas and state there is a header.
    CSVReader = csv.reader(ElectionData_CSVFile,delimiter = ",")
    header = next(CSVReader)

    # Create a variable "TotalVotes" to tally up the total number of votes
    TotalVotes = 0
    # Create a list variable "CandidateList"
    CandidateList = []

    for row in CSVReader:
        # Add 1 to the TotalVotes variable to populate the total votes
        TotalVotes = TotalVotes + 1 

        # Populate CandidateList
        if row[2] not in CandidateList:
            CandidateList.append(row[2])

# Create a variable "CanVote" and set to "0"
CanVote = 0
CanVotePercent = 0.00
HighVotePercent = 0.00
WinnerName = str()
# Print to Terminal and write to text file
# Create and export results to "FinancialAnalysis.txt" file into the Analysis Folder
save_path = 'Analysis'
file_name = "ElectionResults.txt"
CompleteName = os.path.join(save_path,file_name)
file1 = open(CompleteName,"w")

print('Election Results')
file1.write('Election Results\n')
print('----------------------------')
file1.write('----------------------------\n')
print(f'Total Votes: {TotalVotes}')
file1.write(f'Total Votes: {TotalVotes}\n')
print('----------------------------')
file1.write('----------------------------\n')
for Candidate in CandidateList:
    # Open the CSV file
    with open(ElectionData_CSV,encoding='utf') as ElectionData_CSVFile:
        # Split the data on commas and state there is a header.
        CSVReader = csv.reader(ElectionData_CSVFile,delimiter = ",")
        header = next(CSVReader)

        # Look through the spreadsheet and count the candidate's vote
        for row in CSVReader:
            if row[2] == Candidate:
                CanVote = CanVote+1
   # Calculate percentage
    CanVotePercent = CanVote/TotalVotes
    # Format number to %
    CVP_format = "{:.3%}".format(CanVotePercent)
    print(f'{Candidate} {CVP_format} ({CanVote})')
    file1.write(f'{Candidate} {CVP_format} ({CanVote})\n')
    # Work out the winner
    if CanVotePercent > HighVotePercent:
        WinnerName = Candidate
        HighVotePercent = CanVotePercent
    CanVote = 0
print('----------------------------')
file1.write('----------------------------\n')
print(f'Winner: {WinnerName}')
file1.write(f'Winner: {WinnerName}\n')
print('----------------------------')
file1.write('----------------------------')

file1 = open(CompleteName)
file1.close()