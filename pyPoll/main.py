import os
import csv

#set path for the file
csvpath = './Resource/election_data.csv'

#initiate variables
tot_votes = 0

#initiate dictionaries to store the values in each column
candidates = {}


#open the csv file and read
with open(csvpath,'r') as pollfile:
    csvReader = csv.reader(pollfile)
    header = next(csvReader)
    #print(list(csvReader))

    #to calculate total votes
    for row in csvReader:
        tot_votes += 1
        name = row[2]
        #count = int(row[0])

        #to calculate votes per candidate
        if name in candidates:
            candidates[name]['count_total'] += 1
        else:
            candidates[name] = {'count_total': 1}

# for name, candidates_dict in candidates.items():
#     output = '\n'
#     output += f"{name} : {candidates_dict['count_total']}"
#     output += '\n'
# print(output)
    #to count the total votes per candidate
    

output = f"Election Results"
output += '\n--------------------------\n'
output += f"Total votes: {tot_votes}"
output += '\n'
output += '--------------------------\n'
for name, candidates_dict in candidates.items():
    output += f"{name} : {candidates_dict['count_total']}"
    output += '\n'

print(output)
