#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:44:28 2019

@author: nawal
"""

import csv
import matplotlib.pyplot as plt


season = []
match_id = []
total_runs = []
bowling_team = []
overs = []


def readcsvfile():
    teams = []
    with open('matches.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            season.append(row[1])
            if row[1]=='2017':
                if row[4] not in teams:
                    teams.append(row[4])
                    
    csvfile.close()
    
    first_index = season.index('2017')+1
    last_index = season.index('2017')+season.count('2017')
    #print(first_index)
    #print(last_index)
    
    with open('deliveries.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            match_id.append(row[0])
            bowling_team.append(row[3])
            overs.append(row[4])
            total_runs.append(row[17])
    csvfile.close() 
    calculateData(first_index, last_index, teams)
    

def calculateData(first_index, last_index, teams):
    last = match_id.index(str(last_index))+match_id.count(str(last_index))
    first = match_id.index(str(first_index))
    
    economy_list = []
    
    for t in teams:
        runs = 0
        ovr = 0
        for i in range(first, last):
            if 16<=int(overs[i])<=20:
                if bowling_team[i] == t:
                    runs += int(total_runs[i])
                    if overs[i] != overs[i+1]:
                       ovr += 1
        economy_list.append(runs/ovr)
    
    #print(economy_list) 
    print('''
        It all amounts to the fact that Gujarat Lions are the most expensive  
        team during the death overs and, as a result, are struggling to see 
        out matches that they are otherwise in control of. In the depth over  
        It leaks the run approx 9.948 run per over. In other side Sunrieses 
        Hyderabad are less expensive team during the depth over. it has given 
        run of the economy 8.73, One reason of the less expensive of Sunrieses    
        Hydrabad is ,Bhuneshwar Kumar has exprience in the depth over.
    ''')
    plotGraph(teams, economy_list)
    

def plotGraph(teams, economy_list):        
    plt.bar(teams, economy_list, color=['#e67e22', 'b', '#3498db', '#f1c40f', 'r', '#e74c3c', '#8e44ad', 'pink'])
    plt.xticks(rotation='90')
    plt.title("Economy rate in Overs 16-20 of IPL 2017", fontweight="bold")
    plt.xlabel("Teams", fontweight="bold")
    plt.ylabel("Economy", fontweight="bold")
    plt.show()
    

readcsvfile()