#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 20:21:46 2019

@author: nawal
"""

import csv
import matplotlib.pyplot as plt

years = []


# read the csv file
def readcsvFile():
    year = []
    matches = []
    nex = 0
    pre = 0
    last_year = ''
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        
        for row in reader:
              years.append(row[1])
              pre = nex
              if row[1] not in year:
                  year.append(row[1])
                  nex = years.index(row[1])
                  matches.append(nex-pre)
                  last_year = row[1]
    
    csvFile.close()
    login(last_year, matches, year)


# logic function 
def login(last_year, matches, year):
    
    matches.append(years.count(last_year))
    matches = matches[1:]   #remove the first element from list match ,i.e 0
    # Swap the first element in last, now it sorted according to year
    start, *rest = matches
    matches = *rest, start
    
    year.sort()
    #print(year)
    #print(matches)
    plotGraph(year, matches)


def plotGraph(year, matches):
    #Plot Bar Graph
    plt.bar(year, matches, color='y')
    plt.xlabel("Years")
    plt.ylabel("Matches Played")
    plt.show()


readcsvFile()