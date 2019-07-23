#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:14:32 2019

@author: nawal
"""
import matplotlib.pyplot as plt
import csv

years = []

def readcsvFile():
    # Read matches.csv file
    with open('matches.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            years.append(row[1])
    csvFile.close()
    
    #find first and last index of year 2015
    first_index = years.index('2015') + 1
    last_index = years.index('2015') + years.count('2015')
    
    run = {}
    over = {}
    # Read deliveries.csv file
    with open('deliveries.csv') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        for row in reader:
            if int(row[0])>=first_index and int(row[0])<=last_index:
                if row[8] not in run.keys():
                    run[row[8]] = int(row[17])
                    over[row[8]] = 1
                else:
                    run[row[8]] = (run[row[8]]+int(row[17]))
                    over[row[8]] = (over[row[8]]+1)
                    
            elif int(row[0])>last_index:
                break
            
        over_dict = {k:v//6 for k, v in over.items()}
    csvFile.close()
    # Economy of each bowler of 2015
    economy_dict = {k: run[k]/over_dict[k] for k in run.keys() & over_dict}
    # calculate the top 10 economical bowlers
    data = dict(sorted(economy_dict.items(), key=lambda x: x[1], reverse=True)[:10])
    plotgraph(data)

#plot the graph
def plotgraph(data):
    plt.bar(data.keys(), data.values(), color='c')
    plt.title("Top 10 Economical Bowler of Year 2015 IPL", fontweight="bold")
    plt.xticks(rotation='90')
    plt.xlabel("Name Of Bowlers", fontweight='bold')
    plt.ylabel("Economic", fontweight="bold")
    plt.show()


readcsvFile()
