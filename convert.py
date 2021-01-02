import json
import sys

with open('./portals.json.old') as inFile:
    data = json.load(inFile)

clean = {}
for item in data:
    #print("item: ", item)
    #print("data[item]: ", data[item])
    # First item is "ignore" and second item is "portals"
    guids = []
    clean[item] = []
    for entry in data[item]:
        #print("entry: ", entry)
        #print("entry['guid']: ", entry['guid'])
        latlng = entry['latlng'].split(',')
        entry['coordinates'] = {'lat': latlng[0], 'lng': latlng[1]}
        if entry['guid'] in guids:
            print('duplicate guid:' + entry['guid'])
        else:
            guids.append(entry['guid'])
            clean[item].append(entry)
                
with open('./portals.json', 'w') as outFile:
    json.dump(clean, outFile, indent=4, separators=(',', ': '))
