#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 21:30:34 2019

@author: nawal
"""

import matplotlib.pyplot as plt
import csv

years = []


def readcsvFiles():
    #Read seasons from the matches.csv and store in years list
    with open('matches.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
    csvFile.close()
    
    # Find First And Last Index of Year 2016 from match.csv file
    first_index = years.index('2016')+1
    last_index = years.index('2016')+years.count('2016')
    
    # Read the deliveries csv file and caculate usefull data
    extra = {} # dictionary that store team and run
    with open('deliveries.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:   
            if int(row[0])>=first_index and int(row[0])<=last_index:
                if row[3] not in extra.keys():
                    extra[row[3]] = int(row[16])
                else:
                    extra[row[3]] = (extra[row[3]] + int(row[16]))
            elif int(row[0])>last_index:
                break
    csvFile.close()
    plotGraph(extra)
    
    
# Plot Bar Graphs
def plotGraph(extra):
    plt.title("Extra Runs Conceded per Teams in Year 2016 IPL", fontweight="bold")
    plt.bar(extra.keys(), extra.values(), color='b')
    plt.xticks(rotation='90')
    plt.xlabel("Team Names",fontweight='bold')
    plt.ylabel("Extra Runs", fontweight='bold')
    plt.show()
    
    
readcsvFiles()
