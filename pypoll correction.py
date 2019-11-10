# Modules
import os
import csv

# path this file
csvpath = os.path.join('election_data.csv')

# initializing a variable for the election data
data_poll={}
total_votes = 0
candidates = []
Total_number_votes=[]
with open(csvpath, 'r') as data:
    dataread = csv.reader(data)
    next(dataread, None)

    for row in dataread:
        total_votes += 1
        if row[2] in data_poll.keys():
            data_poll[row[2]] = data_poll[row[2]] + 1
        else:
            data_poll[row[2]] = 1
# Total Number of votes during the election
for key, value in data_poll.items():
    candidates.append(key)
    Total_number_votes.append(value)

 # candidate percentage
candidate_percentage = []
for n in Total_number_votes:
    candidate_percentage.append(round(n/total_votes * 100, 1))

# finding winner candidate in this data
format_data = list(zip(candidates, Total_number_votes, candidate_percentage))

winner_list = []
for name in format_data:
    if max(Total_number_votes) == name[1]:
        winner_list.append(name[0])
winner = winner_list[0]

# Print the out come  
print("Election Results :")
print(total_votes)
print(candidates)
print(candidate_percentage)
print(Total_number_votes)
print(winner)

# writing the output data
DataPoll = open("output.txt","w+")
DataPoll.write("Election Results")
DataPoll.write('\n' + "Total_votes" + str(total_votes))
DataPoll.write('\n' + str(candidates))
DataPoll.write('\n' + str(candidate_percentage))
DataPoll.write('\n' + str(Total_number_votes))
DataPoll.write('\n' + "Winner:" + winner)