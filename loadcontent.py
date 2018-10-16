#!/usr/bin/env python3

import csv
import json

out = []
with open('content.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        if all(v for v in row[:5]):  # all elements are filled in
            out.append({'image': row[0] + '.jpg', 'alttext': row[1], 
                'excuse': row[2], 'answer': row[3], 'source': row[4]})

with open('memes.json', 'w') as outfile:
    json.dump(out[1:], outfile) # dump all but the header row

