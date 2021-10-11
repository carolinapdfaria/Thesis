#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:21:53 2021

@author: carolinafaria
"""

# IMPACT-HTA

# 2. Measurement of proximity and similarity of answers

# This file contains the implementation of the evaluation of answers' 
# similarity, between all pairs of stakeholders, as well as the following edges writing.

# This file concerns the IMPACT-HTA project, more specifically, when the 
# "neutral" and "no answer" groups are considered separately.
# In this case, both agreement and conflict are considered.


# We will read .csv files
import csv

# All available files. This list does not present the complete name of the 
# files, only the necessary part for later automatic uses.

files = ['type_AA','type_BB','type_CC','type_DD','type_EE','type_FF',
         'all_items',
         'item_01','item_02','item_03','item_04','item_05','item_06','item_07',
         'item_08','item_09','item_10','item_11','item_12','item_13','item_14',
         'item_15','item_16','item_17','item_18','item_19','item_20','item_21',
         'item_22','item_23']

for file in files:
    # Open the file with the answered data from all stakeholders who were in R2
    with open(file[0:3]+'/'+file[-2:]+'/'+file+'.csv', 'r') as datacsv: 
        # Read the .csv
        datareader = csv.reader(datacsv, delimiter=';') 
        # Retrieve the data 
        data = [n for n in datareader][1:]

    # List of the name of the nodes / stakeholders' number
    data_stakeholders = [n[0] for n in data] 

    # Number of considered aspects
    number_aspects = (len(data[0])-2)

    print('Number of aspects', number_aspects)
    print('Number of stakeholders',len(data_stakeholders))
    print('Stakeholders',(data_stakeholders))
    
    # Function that evaluates the answers of two stakeholders, regarding 
    # a given aspect and attributes a group to that relation
    
    def evaluate_group(aspect1,aspect2):
        if aspect1 == "Strongly agree":
            if aspect2 == "Strongly agree":
                group = 'same answer'
            elif aspect2 == "Agree":
                group = 'same group'
            elif aspect2 == "Disagree":
                group = 'opposite group'
            elif aspect2 == "Strongly disagree":
                group = 'opposite group'
            else:
                group = 'different group'
            
        elif aspect1 == "Agree":
            if aspect2 == "Agree":
                group = 'same answer'
            elif aspect2 == "Strongly agree":
                group = 'same group'
            elif aspect2 == "Disagree":
                group = 'opposite group'
            elif aspect2 == "Strongly disagree":
                group = 'opposite group'
            else:
                group = 'different group'
            
        elif aspect1 == "Strongly disagree":
            if aspect2 == "Strongly disagree":
                group = 'same answer'
            elif aspect2 == "Disagree":
                group = 'same group'
            elif aspect2 == "Agree":
                group = 'opposite group'
            elif aspect2 == "Strongly agree":
                group = 'opposite group'
            else:
                group = 'different group'
            
        elif aspect1 == "Disagree":
            if aspect2 == "Disagree":
                group = 'same answer'
            elif aspect2 == "Strongly disagree":
                group = 'same group'
            elif aspect2 == "Agree":
                group = 'opposite group'
            elif aspect2 == "Strongly agree":
                group = 'opposite group'
            else:
                group = 'different group'
    
        elif aspect1 == "Neither agree nor disagree":
            if aspect2 == "Neither agree nor disagree":
                group = 'same answer'
            elif aspect2 == "Don't know/Don't want to answer":
                group = 'different group'
            else:
                group = 'different group'
            
        elif aspect1 == "Don't know/Don't want to answer":
            if aspect2 == "Neither agree nor disagree":          
                group = 'different group'
            elif aspect2 == "Don't know/Don't want to answer":
                group = 'same answer'
            else:
                group = 'different group'
      

        else:
            group = 'different group'
        
    
        return group

    # Possible threshold values to consider
    # When we are only evaluating one item, no threshold is needed.
    # In that case the score is either 0 or 1. Being higher than zero is enough
    # and the results will be the same for the other options.
    
    if file[0:4] == 'item':

        thresholds = [0]
    else:
        thresholds = [0.4,0.5,0.6,0.7,0.8]
        
    
    # Write the file with the edges 
    for threshold in thresholds:
        with open(file[0:3]+'/'+file[-2:]+'/Edges_'+file+'_'+str(threshold)+'.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['stakeholder1', 'stakeholder2', 'weigth'])
            for n in range( len(data)-1): 
                for i in range(1, len(data)-n): 
                    score_SAA = 0
                    score_SDD = 0
                    f = 1
                    for z in range(2, number_aspects+2):
                    
                        # Attribute a score to each relation

                        if (evaluate_group(data[n][z],data[n+i][z])) == 'same answer': 
                            score_SAA += 1
                    
                        elif (evaluate_group(data[n][z],data[n+i][z])) == 'same group' : 
                            score_SAA += 1
                    
                        elif (evaluate_group(data[n][z],data[n+i][z])) == 'opposite group':
                            score_SDD += 1
                    
                        else:
                            print('We are neutral')

                    print ('Done with these two')
            
                    score_total = score_SAA - score_SDD
                    score = score_total/number_aspects
            
                    # Define threshold          
                    if score > threshold:
                        writer.writerow([data[n][0],data[n+i][0],score])
                    else:
                        # If the score is lower than the stakeholder there is no edge 
                        print("no")
                
