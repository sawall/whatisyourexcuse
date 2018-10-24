#!/usr/bin/env python3

import csv
import json

memes = []

# landing page
memes.append({
    'meme_id': 'index',
    'image': 'eagle.jpg',
    'alt': 'What is your excuse not to vote?',
    'excuse': '',
    'answer': '',
    'link': '',
    'quip': "I've got a great excuse!"
})

with open('content.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        r = [x.replace('\n', '<br/>') for x in row]
        # all elements are filled in and ready is marked
        if len(r) > 7 and all(v for v in r[:7]) and (r[6] == 'yes' or r[6] == 'y'):
            memes.append({
                'meme_id': r[0],
                'image': r[1],
                'alt': r[2],
                'excuse': r[3],
                'answer': r[4],
                'info': r[5], 
                'quip': 'Yeah, AND?'
            })

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('base.html')

# build the site in www
import shutil

shutil.rmtree('www/')
shutil.copytree('static/', 'www/')

for i, meme in enumerate(memes):
    meme['next_meme'] = memes[(i+1) % len(memes)]['meme_id']
    meme['prev_meme'] = memes[(i-1) % len(memes)]['meme_id']
    template.stream(meme=meme).dump('www/' + meme['meme_id'] + '.html')


