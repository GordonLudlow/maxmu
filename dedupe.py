import json
import sys

with open('./portals.json') as inFile:
    data = json.load(inFile)

clean = {}
for item in data:
    #print(item)
    #print(data[item])
    guids = []
    clean[item] = []
    for entry in data[item]:
        #print(entry)
        #print(entry['guid'])
        if entry['guid'] in guids:
            print('duplicate guid:' + entry['guid'])
        else:
            guids.append(entry['guid'])
            clean[item].append(entry)
                
with open('./portals.json.clean', 'w') as outFile:
    json.dump(clean, outFile, indent=4, separators=(',', ': '))
