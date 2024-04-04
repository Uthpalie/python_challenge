import os
import csv

#set path for the file
csvpath = './Resource/election_data.csv'

#open the csv file and read
with open(csvpath,'r') as pollfile:
    csvReader = csv.reader(pollfile)
    header = next(csvReader)
    #print(list(csvReader))

    #count the total number of votes
    tot_votes = 0
    candidate = {}

    for row in csvReader:
        tot_votes += 1
    

    #to count the total votes per candidate

        name = row[2]
        try:
            #stats[name]['count_total'] += votes
            candidate[name]['count_total'] += 1
            # tallies[name] = tallies[name] + points

        except:
            # stats[name]['sum_total'] = points
            # stats[name]['count_total'] = 1
            candidate[name] = {
               'count_total': 1
            }


    #percentage of votes by each candidate

    


    #winner of the election
   
    
print("Election Results")
print("------------------------------------")
print(f"Total votes: {tot_votes} ")
output = '\n'
output += '--------------------------\n'
for name, candidate_dict in candidate.items():
    output += f"{name} : {candidate_dict['count_total']}"
    output += '\n'

print(output)
