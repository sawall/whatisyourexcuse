#!/usr/bin/env python3
import secrets

with open('hashes.txt', 'w') as outfile:
    for i in range(100):
        outfile.write(secrets.token_urlsafe(8) + '\n')
    outfile.close()
