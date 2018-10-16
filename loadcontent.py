#!/usr/bin/env python3

import csv
import json

# BUG: does not deal nicely with " characters

memes = []
with open('content.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        # all elements are filled in and ready is marked
        if all(v for v in row[:5]) and (row[5] == 'yes' or row[5] == 'y'):  
            memes.append((row[0] + '.jpg', row[1], row[2], row[3], row[4]))

with open('static/memes.js', 'w') as outfile:
    outfile.write('''var excuse = [];
var meme = [];
var alt = [];
var footnotes = [];
var info = [];

// loading page
meme.push("eagle.jpg");
alt.push("What is your excuse not to vote?");
excuse.push("");
footnotes.push("");
info.push("");''')
    for m in memes[1:]:  # skip header
        outfile.write('''
meme.push("{}");
alt.push("{}");
excuse.push("{}");
footnotes.push("{}");
info.push("{}");'''.format(*mesc))
    
    outfile.close()


