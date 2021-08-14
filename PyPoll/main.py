# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

import os
import csv

#set variables needed 

candidates = []
number_of_votes = 0
count_of_votes = []

#reading csv for data 
electiondata = r"C:\Users\Antwon\Desktop\DataHomework\Python-Challenge\Python-Challenge\PyPoll\Resources\election_data.csv"

with open(electiondata, 'r') as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvfile)

#looping through data for candidates
    for row in csv_reader:
        number_of_votes = number_of_votes + 1
        candidate = row[2]

        if candidate in candidates:
            candidate_in = candidates.index (candidate)
            count_of_votes[candidate_in] = count_of_votes[candidate_in] + 1
        else: 
            candidates.append(candidate)
            count_of_votes.append(1)

#setting variables for percentages 

percent = []
max_v = count_of_votes[0]
max_i = 0

#calculating percentages and winner of election 

for count in range(len(candidates)):
    percent_vote = count_of_votes[count]/number_of_votes*100
    percent.append(percent_vote)

    if count_of_votes[count] > max_v:
        max_v = count_of_votes[count]

winner = candidates[max_i]

#printing results to the terminal using range, len, and a simple for loop 

print("Election Results")
print("-------------------------")
print(f"Total Votes: {number_of_votes}")
print("-------------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percent[count]}% ({count_of_votes[count]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#output to .txt file in analysis folder 

FinalAnalysis = r"C:\Users\Antwon\Desktop\DataHomework\Python-Challenge\Python-Challenge\PyPoll\Analysis\FinalAnalysis.txt"

with open (FinalAnalysis, 'w') as output:

    output.write("Election Results\n")
    output.write("-------------------------\n")
    output.write(f"Total Votes: {number_of_votes}\n")
    output.write("-------------------------\n")
    for count in range(len(candidates)):
        output.write(f"{candidates[count]}: {percent[count]}% ({count_of_votes[count]})\n")
    output.write("-------------------------\n")
    output.write(f"Winner: {winner}\n")
    output.write("-------------------------\n")



