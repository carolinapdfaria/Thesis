#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:50:33 2021

@author: carolinafaria
"""

# MEDI-VALUE 

# IMPLANTS 

# GROUP A



partitions = [('5769', 1), ('5868', 2), ('10801', 2), ('10847', 2), ('12234', 2), ('13716', 2), ('14601', 2), ('14603', 2), ('14624', 2), ('14628', 3), ('14630', 2), ('14638', 2), ('14640', 2), ('14645', 1), ('14647', 2), ('14654', 3), ('14655', 1), ('14659', 1), ('14665', 2), ('14667', 2), ('14675', 1), ('14677', 1), ('14692', 2), ('14699', 1), ('14708', 2), ('14711', 1), ('14729', 2), ('14752', 2), ('14754', 2), ('14760', 1), ('14785', 1), ('14799', 2), ('14801', 2), ('14806', 2), ('14813', 1), ('14819', 2), ('14823', 2), ('14825', 2), ('14845', 2), ('14846', 2), ('14847', 2), ('14854', 2), ('14857', 1), ('14859', 2), ('14860', 2), ('14865', 1), ('14871', 2), ('14872', 2), ('14876', 1), ('14880', 2), ('14885', 2), ('14886', 1), ('14888', 2), ('14901', 2), ('14903', 2), ('14912', 2), ('14919', 1), ('14931', 2), ('14934', 1), ('14940', 2), ('15195', 2), ('15201', 2), ('15212', 1), ('15215', 2), ('15216', 2), ('15219', 2), ('15220', 2), ('15222', 2), ('15224', 2), ('15229', 2), ('8678', 1), ('8679', 2), ('8733', 2), ('10398', 1), ('10840', 2), ('14233', 1), ('14604', 2), ('14609', 2), ('14612', 1), ('14615', 2), ('14627', 2), ('14629', 0), ('14634', 3), ('14646', 3), ('14671', 3), ('14685', 2), ('14688', 3), ('14691', 2), ('14697', 2), ('14714', 2), ('14719', 2), ('14738', 1), ('14746', 2), ('14753', 2), ('14772', 2), ('14778', 2), ('14784', 1), ('14787', 2), ('14817', 2), ('14818', 2), ('14834', 2), ('14838', 2), ('14840', 2), ('14841', 3), ('14842', 2), ('14843', 2), ('14848', 2), ('14858', 2), ('14861', 1), ('14866', 1), ('14867', 2), ('14868', 2), ('14873', 2), ('14874', 2), ('14879', 2), ('14883', 2), ('14889', 2), ('14890', 2), ('14894', 1), ('14899', 2), ('14900', 3), ('14942', 2), ('15041', 2), ('15085', 2), ('15091', 2), ('15189', 2), ('15191', 2), ('15194', 1), ('15206', 2), ('15210', 2), ('15211', 2), ('15218', 2), ('15225', 1), ('15232', 3)]

community_1 = []
community_2 = []
community_3 = []
community_4 = []

for item in partitions:
    if item [1] == 2:
        community_1.append(item[0])
    elif item [1] == 1:
        community_2.append(item[0])
    elif item [1] == 3:
        community_3.append(item[0])
    elif item [1] == 0:
        community_4.append(item[0])


            
import csv

with open('type_AA.csv', 'r') as datacsv: 
    # Read the .csv
    datareader = csv.reader(datacsv, delimiter=';') 
    # Retrieve the data 
    data = [n for n in datareader][1:]
    
stakeholders_id = [n[0] for n in data] 

# List of [[Stakeholder,answer]]
#[n[0],n[2]....n[number_of_aspects+1]]
stakeholders_answers = [[n[0],n[2],n[3],n[4],n[5]] for n in data]




answers_options = ['Critical','Fundamental','Complementary','Irrelevant',"Don't know / Don't want to answer"]



# community 1

include_high_1 = 0
include_low_1 = 0
not_include_1 = 0
no_answer_1 = 0
for stakeholder_C1 in community_1:

    for i in range (len(stakeholders_answers)):
        if stakeholder_C1 == stakeholders_answers[i][0]:
                for j in range(4):
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
                for j in range(4):
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
                for j in range(4):
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
                for j in range(4):
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


    
import networkx as nx
import matplotlib.pyplot as plt
        

Group_A = nx.Graph()
top_nodes = ['C1', 'C2','C3'
             #,'C4'
             ]
bottom_nodes = ['I+','I-','DNI','NA']

Group_A.add_nodes_from(top_nodes, bipartite=0)
Group_A.add_nodes_from(bottom_nodes, bipartite=1)



Group_A.add_weighted_edges_from([('C1','I+',include_high_1/(len(community_1)*4)*10),
                                 ('C2','I+',include_high_2/(len(community_2)*4)*10),
                                 ('C3','I+',include_high_3/(len(community_3)*4)*10),
                                 #('C4','I+',include_high_4/(len(community_4)*4)*10),
                                 ('C1','I-',include_low_1/(len(community_1)*4)*10),
                                 ('C2','I-',include_low_2/(len(community_2)*4)*10),
                                 ('C3','I-',include_low_3/(len(community_3)*4)*10),
                                 #('C4','I-',include_low_4/(len(community_4)*4)*10),
                                 ('C1','DNI',not_include_1/(len(community_1)*4)*10),
                                 ('C2','DNI',not_include_2/(len(community_2)*4)*10),
                                 ('C3','DNI',not_include_3/(len(community_3)*4)*10),
                                 #('C4','DNI',not_include_4/(len(community_4)*4)*10),
                                 ('C1','NA',no_answer_1/(len(community_1)*4)*10),
                                 ('C2','NA',no_answer_2/(len(community_2)*4)*10),
                                 ('C3','NA',no_answer_3/(len(community_3)*4)*10),
                                 #('C4','NA',no_answer_4/(len(community_4)*4)*10)
                                 ])

top = nx.bipartite.sets(Group_A)[0]
pos = nx.bipartite_layout(Group_A, top)

pos['C1'] = (0, 1)

pos['C2'] = (0, 0)

pos['C3'] = (0, -1)

#pos['C4'] = (0, -2)


pos['I+'] = (1, 1)

pos['I-'] = (1, 0)

pos['DNI'] = (1, -1)

pos['NA'] = (1, -2)


edges = Group_A.edges()
weights = [Group_A[u][v]['weight'] for u,v in edges]

nx.draw(Group_A, pos=pos,
        #node_size=1000, 
        with_labels=True,
        width=weights,
        #node_color=['hotpink','deepskyblue','palegreen','gold','grey','grey','grey','grey'],
         )

from networkx import *

nodes = nx.draw_networkx_nodes(Group_A, pos=pos, 
                               node_size=650,
                               node_color = 'white',
                               edgecolors = 'black')


nx.draw_networkx_edge_labels(Group_A,pos,edge_labels={
    ('C1','I+'):include_high_1,
    ('C2','I+'):include_high_2,
    ('C3','I+'):include_high_3,
    #('C4','I+'):include_high_4,
    ('C1','I-'):include_low_1,
    ('C2','I-'):include_low_2,
    ('C3','I-'):include_low_3,
    #('C4','I-'):include_low_4,
    ('C1','DNI'):not_include_1,
    ('C2','DNI'):not_include_2,
    ('C3','DNI'):not_include_3,
    #('C4','DNI'):not_include_4,
    ('C1','NA'):no_answer_1,
    ('C2','NA'):no_answer_2,
    ('C3','NA'):no_answer_3,
   # ('C4','NA'):no_answer_4
    
    },
    font_color='black',
    label_pos=0.2)

plt.savefig('MEDI_IMD_Group_A.pdf', format='pdf',bbox_inches='tight',transparent=True)
plt.show()



B = nx.Graph()
B.add_nodes_from([1,2,3,4], bipartite=0) # Add the node attribute "bipartite"
B.add_nodes_from(['abc','bcd','cef'], bipartite=1)
B.add_edges_from([(1,'abc'), (1,'bcd'), (2,'bcd'), (2,'cef'), (3,'cef'), (4,'abc')])




