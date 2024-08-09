import csv

def saveCSVData(input, fileName):
    data = []
    for entry in input:
        tactic = entry['tactic']
        techniques = entry['techniques']
        if not techniques:
            data.append({'Tactic': tactic, 'Technique': 'No Instances', 'Count': 0})
        for technique in techniques:
            data.append({'Tactic': tactic, 'Technique': technique['name'], 'Count': int(technique['count'])})
    
    header = data[0].keys()
    with open(fileName, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
