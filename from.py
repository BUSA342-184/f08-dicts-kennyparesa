#!/usr/bin/env python3 
"""
Assignment 08

This program reads a file and parses out user names and domain names to a csv list.
"""
import sys
import csv

# initialize dictionaries to add to
userFrom = {}
userTo = {}
hostFrom = {}
hostTo = {}

# opens the file  
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:' ) or line.startswith('To:' ):
        # split the lines into indivdual strings
        words = line.split()
        # split the email from either From or To
        email = words[1]
        # splits the email addresses into user names and the domain name
        user, host = email.split('@')
        # adds the username and the host name to the respective dictionaries
        if line.startswith('From:'):
            userFrom[user] = userFrom.get(user, 0) + 1
            hostFrom[host] = hostFrom.get(host, 0) + 1
        else:
            userTo[user] = userTo.get(user, 0) + 1
            hostTo[host] = hostTo.get(host, 0) + 1 

# create the csv list 
csvWrite = csv.writer(sys.stdout)

# prints out the csv list into different sections and displays contents
print('--- FROM USER ---')
csvWrite.writerows(sorted(userFrom.items()))
print('--- FROM HOST ---')
csvWrite.writerows(sorted(hostFrom.items()))
print('--- TO USER ---')
csvWrite.writerows(sorted(userTo.items()))
print('--- TO HOST ---')
csvWrite.writerows(sorted(hostTo.items()))
