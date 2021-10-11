#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:50:33 2021

@author: carolinafaria
"""

# MEDI-VALUE 

# IMPLANTS 

# ALL



partitions = [('5769', 5), ('5868', 1), ('10801', 1), ('10847', 5), ('12234', 5), ('13716', 1), ('14601', 1), ('14603', 1), ('14624', 1), ('14628', 0), ('14630', 1), ('14638', 1), ('14640', 1), ('14645', 3), ('14647', 1), ('14654', 0), ('14655', 3), ('14659', 5), ('14665', 1), ('14667', 1), ('14675', 5), ('14677', 1), ('14692', 1), ('14699', 5), ('14708', 5), ('14711', 4), ('14729', 5), ('14752', 3), ('14754', 5), ('14760', 5), ('14785', 5), ('14799', 1), ('14801', 3), ('14806', 5), ('14813', 1), ('14819', 3), ('14823', 5), ('14825', 3), ('14845', 5), ('14846', 1), ('14847', 5), ('14854', 5), ('14857', 3), ('14859', 3), ('14860', 5), ('14865', 1), ('14871', 3), ('14872', 1), ('14876', 5), ('14880', 3), ('14885', 3), ('14886', 1), ('14888', 1), ('14901', 1), ('14903', 1), ('14912', 1), ('14919', 5), ('14931', 3), ('14934', 1), ('14940', 3), ('15195', 1), ('15201', 5), ('15212', 1), ('15215', 5), ('15216', 3), ('15219', 1), ('15220', 1), ('15222', 5), ('15224', 5), ('15229', 5), ('8678', 5), ('8679', 1), ('8733', 1), ('10398', 3), ('10840', 3), ('14233', 1), ('14604', 1), ('14609', 5), ('14612', 1), ('14615', 1), ('14627', 5), ('14629', 2), ('14634', 0), ('14646', 0), ('14671', 0), ('14685', 3), ('14688', 0), ('14691', 5), ('14697', 1), ('14714', 1), ('14719', 3), ('14738', 1), ('14746', 1), ('14753', 1), ('14772', 1), ('14778', 5), ('14784', 5), ('14787', 3), ('14817', 3), ('14818', 3), ('14834', 5), ('14838', 5), ('14840', 5), ('14841', 0), ('14842', 1), ('14843', 1), ('14848', 3), ('14858', 1), ('14861', 5), ('14866', 3), ('14867', 1), ('14868', 5), ('14873', 1), ('14874', 1), ('14879', 1), ('14883', 1), ('14889', 3), ('14890', 3), ('14894', 3), ('14899', 3), ('14900', 0), ('14942', 1), ('15041', 1), ('15085', 1), ('15091', 1), ('15189', 3), ('15191', 5), ('15194', 3), ('15206', 1), ('15210', 1), ('15211', 1), ('15218', 1), ('15225', 1), ('15232', 0)]

community_1 = []
community_2 = []
community_3 = []
community_4 = []
community_5 = []
community_6 = []

for item in partitions:
    if item [1] == 1:
        community_1.append(item[0])
    elif item [1] == 5:
        community_2.append(item[0])
    elif item [1] == 3:
        community_3.append(item[0])
    elif item [1] == 0:
        community_4.append(item[0])
    elif item [1] == 2:
        community_5.append(item[0])
    elif item [1] == 4:
        community_6.append(item[0])


            
import csv

with open('all_items.csv', 'r') as datacsv: 
    # Read the .csv
    datareader = csv.reader(datacsv, delimiter=';') 
    # Retrieve the data 
    data = [n for n in datareader][1:]
    
stakeholders_id = [n[0] for n in data] 

# List of [[Stakeholder,answer]]
#[n[0],n[2]....n[number_of_aspects+1]]
stakeholders_answers = [[n[0],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9],n[10],n[11],
                         n[12],n[13],n[14],n[15],n[16],n[17],n[18],n[19],n[20],n[21],
                         n[22],n[23],
                         n[24],n[25],n[26],n[27],n[28],n[29],n[30],n[31]
                         ,n[32],n[33],n[34],n[35]] for n in data]




answers_options = ['Critical','Fundamental','Complementary','Irrelevant',"Don't know / Don't want to answer"]



# community 1

include_high_1 = 0
include_low_1 = 0
not_include_1 = 0
no_answer_1 = 0
for stakeholder_C1 in community_1:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C1 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_1 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_1 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_1 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_1 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_1 += 1
print ('Community 1')
print ('include_high',include_high_1)
print ('include_low',include_low_1)
print ('not_include',not_include_1)
print ('no_answer',no_answer_1)
                        

# community 2

include_high_2 = 0
include_low_2 = 0
not_include_2 = 0
no_answer_2 = 0
for stakeholder_C2 in community_2:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C2 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_2 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_2 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_2 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_2 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_2 += 1
print ('Community 2')
print ('include_high',include_high_2)
print ('include_low',include_low_2)
print ('not_include',not_include_2)
print ('no_answer',no_answer_2)
    


# community 3

include_high_3 = 0
include_low_3 = 0
not_include_3 = 0
no_answer_3 = 0
for stakeholder_C3 in community_3:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C3 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_3 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_3 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_3 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_3 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_3 += 1
print ('Community 3')
print ('include_high',include_high_3)
print ('include_low',include_low_3)
print ('not_include',not_include_3)
print ('no_answer',no_answer_3)




# community 4

include_high_4 = 0
include_low_4 = 0
not_include_4 = 0
no_answer_4 = 0
for stakeholder_C4 in community_4:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C4 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_4 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_4 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_4 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_4 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_4 += 1
print ('Community 4')
print ('include_high',include_high_4)
print ('include_low',include_low_4)
print ('not_include',not_include_4)
print ('no_answer',no_answer_4)


# community 5

include_high_5 = 0
include_low_5 = 0
not_include_5 = 0
no_answer_5 = 0
for stakeholder_C5 in community_5:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C5 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_5 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_5 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_5 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_5 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_5 += 1
print ('Community 5')
print ('include_high',include_high_5)
print ('include_low',include_low_5)
print ('not_include',not_include_5)
print ('no_answer',no_answer_5)


# community 6

include_high_6 = 0
include_low_6 = 0
not_include_6 = 0
no_answer_6 = 0
for stakeholder_C6 in community_6:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C6 == stakeholders_answers[i][0]:
                for j in range(34):
                    if stakeholders_answers[i][j+1] == 'Critical':
                        include_high_6 += 1
                    elif stakeholders_answers[i][j+1] == 'Fundamental':
                        include_high_6 += 1
                    elif stakeholders_answers[i][j+1] == 'Complementary':
                        include_low_6 += 1
                    elif stakeholders_answers[i][j+1] == 'Irrelevant':
                        not_include_6 += 1
                    elif stakeholders_answers[i][j+1] == "Don't know / Don't want to answer":
                        no_answer_6 += 1
print ('Community 6')
print ('include_high',include_high_6)
print ('include_low',include_low_6)
print ('not_include',not_include_6)
print ('no_answer',no_answer_6)

    
import networkx as nx
import matplotlib.pyplot as plt
        

Group_A = nx.Graph()
top_nodes = ['C1', 'C2','C3','C4']
bottom_nodes = ['I+','I-','DNI','NA']

Group_A.add_nodes_from(top_nodes, bipartite=0)
Group_A.add_nodes_from(bottom_nodes, bipartite=1)



Group_A.add_weighted_edges_from([('C1','I+',include_high_1/(len(community_1)*34)*10),
                                 ('C2','I+',include_high_2/(len(community_2)*34)*10),
                                 ('C3','I+',include_high_3/(len(community_3)*34)*10),
                                 ('C4','I+',include_high_4/(len(community_4)*34)*10),
                                 
                                 ('C1','I-',include_low_1/(len(community_1)*34)*10),
                                 ('C2','I-',include_low_2/(len(community_2)*34)*10),
                                 ('C3','I-',include_low_3/(len(community_3)*34)*10),
                                 ('C4','I-',include_low_4/(len(community_4)*34)*10),
                                 
                                 ('C1','DNI',not_include_1/(len(community_1)*34)*10),
                                 ('C2','DNI',not_include_2/(len(community_2)*34)*10),
                                 ('C3','DNI',not_include_3/(len(community_3)*34)*10),
                                 ('C4','DNI',not_include_4/(len(community_4)*34)*10),
                                 
                                 ('C1','NA',no_answer_1/(len(community_1)*34)*10),
                                 ('C2','NA',no_answer_2/(len(community_2)*34)*10),
                                 ('C3','NA',no_answer_3/(len(community_3)*34)*10),
                                 ('C4','NA',no_answer_4/(len(community_4)*34)*10),
                                 
                                 ])

top = nx.bipartite.sets(Group_A)[0]
pos = nx.bipartite_layout(Group_A, top)

pos['C1'] = (0, 1)

pos['C2'] = (0, 0)

pos['C3'] = (0, -1)

pos['C4'] = (0, -2)


pos['I+'] = (1, 1)

pos['I-'] = (1, 0)

pos['DNI'] = (1, -1)

pos['NA'] = (1, -2)


edges = Group_A.edges()
weights = [Group_A[u][v]['weight'] for u,v in edges]

nx.draw(Group_A, pos=pos,
        #node_size=1000, 
        with_labels=True,
        width=weights)

from networkx import *

nodes = nx.draw_networkx_nodes(Group_A, pos=pos, 
                               node_size=650,
                               node_color = 'white',
                               edgecolors = 'black')


nx.draw_networkx_edge_labels(Group_A,pos,edge_labels={
    ('C1','I+'):include_high_1,
    ('C2','I+'):include_high_2,
    ('C3','I+'):include_high_3,
    ('C4','I+'):include_high_4,
    ('C1','I-'):include_low_1,
    ('C2','I-'):include_low_2,
    ('C3','I-'):include_low_3,
    ('C4','I-'):include_low_4,
    ('C1','DNI'):not_include_1,
    ('C2','DNI'):not_include_2,
    ('C3','DNI'):not_include_3,
    ('C4','DNI'):not_include_4,
    ('C1','NA'):no_answer_1,
    ('C2','NA'):no_answer_2,
    ('C3','NA'):no_answer_3,
    ('C4','NA'):no_answer_4,
    
    },
    font_color='black',
    label_pos=0.2)

plt.savefig('MEDI_IMD_Group_A.pdf', format='pdf',bbox_inches='tight',transparent=True)
plt.show()



B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(['abc','bcd','cef'], bipartite=1)
B.add_edges_from([(1,'abc'), (1,'bcd'), (2,'bcd'), (2,'cef'), (3,'cef'), (4,'abc')])




