#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:30:34 2019

@author: nawal
"""

import matplotlib.pyplot as plt
import csv

match_id = []
years = []
bowling_team = []
extra_run = []


def readcsvFiles():
    # Read the deliveries csv file
    with open('deliveries.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            match_id.append(row[0])
            extra_run.append(row[16])
            bowling_team.append(row[3])
    csvFile.close()
    
    # Read the matches.csv file
    team = []
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
            if row[1] == '2016':
                if row[4] not in team:
                    team.append(row[4])
    csvFile.close()
    
    #call logic function
    logic(team)


def logic(team):
    # Find First And Last Index of Year 2016 from match.csv file
    first_index = str(years.index('2016'))
    last_index = str(years.index('2016')+years.count('2016'))
    
    # Logic Of find Extra Runs given by teams
    extra = []
    for t in team:
        count = 0
        for i in range(match_id.index(first_index), match_id.index(last_index)+match_id.count(last_index)):
            if bowling_team[i] == t:
                count += int(extra_run[i])   
        extra.append(count)
    
    #call plotGraph function
    plotGraph(team, extra)
    
    
def plotGraph(team, extra):
    # Plot Bar Graphs
    plt.title("Extra Runs Conceded per Teams in Year 2016 IPL", fontweight="bold")
    plt.bar(team, extra, color='b')
    plt.xticks(rotation='90')
    plt.xlabel("Team Names",fontweight='bold')
    plt.ylabel("Extra Runs", fontweight='bold')
    plt.show()
    
    
readcsvFiles()