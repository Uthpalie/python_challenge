import os
import csv

#set path for the file
csvpath = './Resource/election_data.csv'

#initiate variables
tot_votes = 0
winner = ""
max_vote = 0


#initiate dictionaries to store the values
candidates = {}


#open the csv file and read
with open(csvpath,'r') as pollfile:
    csvReader = csv.reader(pollfile)
    header = next(csvReader)

    #to calculate total votes
    for row in csvReader:
        tot_votes += 1
        name = row[2]

        #to calculate votes per candidate
        if name in candidates:
            candidates[name]['count_total'] += 1
        else:
            candidates[name] = {'count_total': 1}
    
    

output = f"Election Results"
output += '\n--------------------------\n'
output += f"Total votes: {tot_votes}"
output += '\n'
output += '--------------------------\n'
for name, candidates_dict in candidates.items():
    output += f"{name} : {candidates_dict['count_total']/tot_votes*100:.3f}% ({candidates_dict['count_total']})"
    output += '\n'
    if candidates_dict['count_total'] > max_vote:
        max_vote = candidates_dict['count_total']
        winner = name
    else:
        min_vote = candidates_dict['count_total']
output += '--------------------------\n'
output += f"Winner: {winner}\n"
output += '--------------------------\n'   
print(output)

#to write the results to a text file

with open('./Analysis/results.txt','w') as Resultsfile:
    Resultsfile.write(output)