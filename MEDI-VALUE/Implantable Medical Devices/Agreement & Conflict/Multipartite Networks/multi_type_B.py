#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 22:24:33 2021

@author: carolinafaria
"""


# MEDI-VALUE 

# IMPLANTS 

# GROUP B

            
import csv

with open('type_BB.csv', 'r') as datacsv: 
    # Read the .csv
    datareader = csv.reader(datacsv, delimiter=';') 
    # Retrieve the data 
    data = [n for n in datareader][1:]
    
stakeholders_id = [n[0] for n in data] 

# List of [[Stakeholder,answer]]
#[n[0],n[2]....n[number_of_items+1]]
stakeholders_answers = [[n[0],n[2],n[3],n[4]] for n in data]

answers_options = ['Critical','Fundamental','Complementary','Irrelevant',"Don't know / Don't want to answer"]



# HCP

include_high_HCP = 0
include_low_HCP = 0
not_include_HCP = 0
no_answer_HCP = 0

    
for i in range (len(data)):
    print(data[i])
        
    if data[i][1] == 'Healthcare professionals (doctors, nurses, pharmacists, technicians)':
        for j in range(4): # number of aspects
            if data[i][j+2] == 'Critical':
                include_high_HCP += 1
            elif data[i][j+2] == 'Fundamental':
                include_high_HCP += 1
            elif data[i][j+2] == 'Complementary':
                include_low_HCP += 1
            elif data[i][j+2] == 'Irrelevant':
                not_include_HCP += 1
            elif data[i][j+2] == "Don't know / Don't want to answer":
                no_answer_HCP += 1
print ('HCP')
print ('include_high',include_high_HCP)
print ('include_low',include_low_HCP)
print ('not_include',not_include_HCP)
print ('no_answer',no_answer_HCP)







# PC

include_high_PC = 0
include_low_PC = 0
not_include_PC= 0
no_answer_PC = 0

    
for i in range (len(data)):
    print(data[i])
        
    if data[i][1] == 'Patients and citizens':
        for j in range(4): # number of aspects
            if data[i][j+2] == 'Critical':
                include_high_PC += 1
            elif data[i][j+2] == 'Fundamental':
                include_high_PC += 1
            elif data[i][j+2] == 'Complementary':
                include_low_PC += 1
            elif data[i][j+2] == 'Irrelevant':
                not_include_PC += 1
            elif data[i][j+2] == "Don't know / Don't want to answer":
                no_answer_PC += 1
print ('PC')
print ('include_high',include_high_PC)
print ('include_low',include_low_PC)
print ('not_include',not_include_PC)
print ('no_answer',no_answer_PC)







# INDUSTRY

include_high_I = 0
include_low_I = 0
not_include_I= 0
no_answer_I = 0

    
for i in range (len(data)):
    print(data[i])
        
    if data[i][1] == 'Industry':
        for j in range(4): # number of aspects
            if data[i][j+2] == 'Critical':
                include_high_I += 1
            elif data[i][j+2] == 'Fundamental':
                include_high_I += 1
            elif data[i][j+2] == 'Complementary':
                include_low_I += 1
            elif data[i][j+2] == 'Irrelevant':
                not_include_I += 1
            elif data[i][j+2] == "Don't know / Don't want to answer":
                no_answer_I += 1
print ('Industry')
print ('include_high',include_high_I)
print ('include_low',include_low_I)
print ('not_include',not_include_I)
print ('no_answer',no_answer_I)







# Buyers

include_high_BPA = 0
include_low_BPA = 0
not_include_BPA= 0
no_answer_BPA = 0

    
for i in range (len(data)):
    print(data[i])
        
    if data[i][1] == 'Buyers, policymakers and academics':
        for j in range(4):# number of aspects
            if data[i][j+2] == 'Critical':
                include_high_BPA += 1
            elif data[i][j+2] == 'Fundamental':
                include_high_BPA += 1
            elif data[i][j+2] == 'Complementary':
                include_low_BPA += 1
            elif data[i][j+2] == 'Irrelevant':
                not_include_BPA += 1
            elif data[i][j+2] == "Don't know / Don't want to answer":
                no_answer_BPA += 1
print ('BPA')
print ('include_high',include_high_BPA)
print ('include_low',include_low_BPA)
print ('not_include',not_include_BPA)
print ('no_answer',no_answer_BPA)






import networkx as nx
import matplotlib.pyplot as plt
        

Group_B = nx.Graph()
top_nodes = ['HCP', 'PC','I','BPA']
bottom_nodes = ['I+','I-','DNI','NA']

Group_B.add_nodes_from(bottom_nodes, bipartite=0)
Group_B.add_nodes_from(top_nodes, bipartite=1)



Group_B.add_weighted_edges_from([('I+','HCP',include_high_HCP/(60*4)*10),
                                 ('I+','PC',include_high_PC/(28*4)*10),
                                 ('I+','I',include_high_I/(15*4)*10),
                                 ('I+','BPA',include_high_BPA/(31*4)*10),
                                 ('I-','HCP',include_low_HCP/(60*4)*10),
                                 ('I-','PC',include_low_PC/(28*4)*10),
                                 ('I-','I',include_low_I/(15*4)*10),
                                 ('I-','BPA',include_low_BPA/(31*4)*10),
                                 ('DNI','HCP',not_include_HCP/(60*4)*10),
                                 ('DNI','PC',not_include_PC/(28*4)*10),
                                 ('DNI','I',not_include_I/(15*4)*10),
                                 ('DNI','BPA',not_include_BPA/(31*4)*10),
                                 ('NA','HCP',no_answer_HCP/(60*4)*10),
                                 ('NA','PC',no_answer_PC/(28*4)*10),
                                 ('NA','I',no_answer_I/(15*4)*10),
                                 ('NA','BPA',no_answer_BPA/(31*4)*10)
                                 ])

top = nx.bipartite.sets(Group_B)[0]
pos = nx.bipartite_layout(Group_B, top)

pos['HCP'] = (1, 1)

pos['PC'] = (1, 0)

pos['I'] = (1, -1)

pos['BPA'] = (1, -2)


pos['I+'] = (0, 1)

pos['I-'] = (0, 0)

pos['DNI'] = (0, -1)

pos['NA'] = (0, -2)


edges = Group_B.edges()
weights = [Group_B[u][v]['weight'] for u,v in edges]

nx.draw(Group_B, pos=pos,
        #node_size=1000, 
        with_labels=True,
        width=weights,
        node_color=['hotpink','deepskyblue','palegreen','gold','grey','grey','grey','grey'],
         )

from networkx import *

nodes = nx.draw_networkx_nodes(Group_B, pos=pos, 
                               node_size=650,
                               node_color = 'white',
                               edgecolors = 'black')



nx.draw_networkx_edge_labels(Group_B,pos,edge_labels={
    ('HCP','I+'):include_high_HCP,
    ('PC','I+'):include_high_PC,
    ('I','I+'):include_high_I,
    ('BPA','I+'):include_high_BPA,
    ('HCP','I-'):include_low_HCP,
    ('PC','I-'):include_low_PC,
    ('I','I-'):include_low_I,
    ('BPA','I-'):include_low_BPA,
    ('HCP','DNI'):not_include_HCP,
    ('PC','DNI'):not_include_PC,
    ('I','DNI'):not_include_I,
    ('BPA','DNI'):not_include_BPA,
    ('HCP','NA'):no_answer_HCP,
    ('PC','NA'):no_answer_PC,
    ('I','NA'):no_answer_I,
    ('BPA','NA'):no_answer_BPA
    
    },
    font_color='black',
    label_pos=0.2)

plt.savefig('MEDI_IMD_Group_B_Types.pdf', format='pdf',bbox_inches='tight',transparent=True)
plt.show()




