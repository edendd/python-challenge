# Modules
import os
import csv

# path this file
input ="C:/Users/edenh/OneDrive/Desktop/Python Final/pypoll.txt"
output ="C:/Users/edenh/OneDrive/Desktop/Python Final/pypoll.txt"

# Read the File
# initializing a variable for the election
total_votes = 0
candidates = {}
candidate_percentage = []
winner_candidate = ""
winning_count = 0
with open(input, newline = "") as data:
    data_reader = csv.reader(data, delimiter = ",")
    next(data_reader, None)
# For row my csv reader count total number of months
#Find the total number votes
    for row in data_reader:
        total_votes = total_votes + 1
#Find the list of candidates for each row

    for row in data_reader:
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
    else:
        candidates[row[2]] = 1

        # we can find the percentages by putting  each  information from items in the candidates dictionary
        # candidates dictionary
        #key= Name value= total_votes
        for key, value in candidates.items():
            candidate_percentage[key] = round((value/total_votes) * 100, 1)

        # Finding the winner using the candidates dictionary. 
        for key in candidates.keys():
            if candidates[key] > winner_candidate:
                winner = key
                winner_candidate = candidates[key]
# Print the out come  
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidate_percentage[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# writing the new file
with open(output, 'w') as file:
    file.write("Election Results \n")
    file.write("------------------------------------- \n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("------------------------------------- \n")
    for key, value in candidates.items():
        file.write(key + ": " + str(candidate_percentage[key]) + "% (" + str(value) + ") \n")
    file.write("------------------------------------- \n")
    file.write("Winner: " + winner + "\n")
    file.write("------------------------------------- \n")