import csv

inputPath = './resources/test.csv'

with open(inputPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    header = next(csvReader)
    # print(list(csvReader))

    # tally points of each name
    # tallies = {}
    # counts = {}
    stats = {}
    total_rows = 0

    for row in csvReader:
        total_rows += 1
        name = row[0]
        points = int(row[1])
        try:
            stats[name]['sum_total'] += points
            stats[name]['count_total'] += 1
            # tallies[name] = tallies[name] + points

        except:
            # stats[name]['sum_total'] = points
            # stats[name]['count_total'] = 1
            stats[name] = {
                'sum_total': points,
                'count_total': 1
            }

output = 'Read out\n'
output += '=====================\n'
for name, stat_dict in stats.items():
    stat_avg = stat_dict['sum_total']/stat_dict['count_total']
    output += f"{name} received {stat_dict['sum_total']} total points over {stat_dict['count_total']} games with an average of {stat_avg} points per game.\n"
    output += '=====================\n'

print(output)

with open('./output.txt', 'w') as outputFile:
    outputFile.write(output)
