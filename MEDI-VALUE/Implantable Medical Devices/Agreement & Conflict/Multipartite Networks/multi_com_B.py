#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:50:33 2021

@author: carolinafaria
"""

# MEDI-VALUE 

# IMPLANTS 

# GROUP B



partitions = [('5769', 0), ('5868', 1), ('10801', 1), ('10847', 0), ('12234', 0), ('13716', 1), ('14601', 1), ('14603', 1), ('14624', 1), ('14628', 2), ('14630', 1), ('14638', 1), ('14640', 1), ('14645', 1), ('14647', 1), ('14654', 2), ('14655', 1), ('14659', 0), ('14665', 1), ('14667', 1), ('14675', 1), ('14677', 1), ('14692', 1), ('14699', 1), ('14708', 0), ('14711', 0), ('14729', 1), ('14752', 1), ('14754', 0), ('14760', 1), ('14785', 0), ('14799', 1), ('14801', 1), ('14806', 0), ('14813', 1), ('14819', 1), ('14823', 1), ('14825', 1), ('14845', 0), ('14846', 1), ('14847', 1), ('14854', 0), ('14857', 1), ('14859', 1), ('14860', 1), ('14865', 1), ('14871', 1), ('14872', 1), ('14876', 0), ('14880', 1), ('14885', 1), ('14886', 0), ('14888', 1), ('14901', 1), ('14903', 1), ('14912', 0), ('14919', 0), ('14931', 1), ('14934', 1), ('14940', 1), ('15195', 1), ('15201', 0), ('15212', 1), ('15215', 1), ('15216', 1), ('15219', 1), ('15220', 1), ('15222', 0), ('15224', 0), ('15229', 0), ('8678', 0), ('8679', 1), ('8733', 1), ('10398', 1), ('10840', 1), ('14233', 1), ('14604', 1), ('14609', 1), ('14612', 1), ('14615', 1), ('14627', 0), ('14629', 1), ('14634', 2), ('14646', 2), ('14671', 2), ('14685', 1), ('14688', 2), ('14691', 1), ('14697', 1), ('14714', 1), ('14719', 1), ('14738', 1), ('14746', 1), ('14753', 1), ('14772', 0), ('14778', 1), ('14784', 1), ('14787', 1), ('14817', 1), ('14818', 1), ('14834', 0), ('14838', 0), ('14840', 1), ('14841', 2), ('14842', 1), ('14843', 1), ('14848', 0), ('14858', 1), ('14861', 0), ('14866', 1), ('14867', 1), ('14868', 1), ('14873', 1), ('14874', 1), ('14879', 0), ('14883', 1), ('14889', 1), ('14890', 1), ('14894', 1), ('14899', 1), ('14900', 2), ('14942', 1), ('15041', 1), ('15085', 1), ('15091', 1), ('15189', 0), ('15191', 1), ('15194', 1), ('15206', 1), ('15210', 1), ('15211', 1), ('15218', 1), ('15225', 1), ('15232', 2)]


community_1 = []
community_2 = []
community_3 = []
    

for item in partitions:
    if item [1] == 1:
        community_1.append(item[0])
    elif item [1] == 0:
        community_2.append(item[0])
    elif item [1] == 2:
        community_3.append(item[0])
       


            
import csv

with open('type_BB.csv', 'r') as datacsv: 
    # Read the .csv
    datareader = csv.reader(datacsv, delimiter=';') 
    # Retrieve the data 
    data = [n for n in datareader][1:]
    
stakeholders_id = [n[0] for n in data] 

# List of [[Stakeholder,answer]]
#[n[0],n[2]....n[number_of_items+1]]
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



    
import networkx as nx
import matplotlib.pyplot as plt
        

Group_B = nx.Graph()
top_nodes = ['C1', 'C2','C3']
bottom_nodes = ['I+','I-','DNI','NA']

Group_B.add_nodes_from(top_nodes, bipartite=0)
Group_B.add_nodes_from(bottom_nodes, bipartite=1)



Group_B.add_weighted_edges_from([('C1','I+',include_high_1/(len(community_1)*4)*10),
                                 ('C2','I+',include_high_2/(len(community_2)*4)*10),
                                 ('C3','I+',include_high_3/(len(community_3)*4)*10),

                                 ('C1','I-',include_low_1/(len(community_1)*4)*10),
                                 ('C2','I-',include_low_2/(len(community_2)*4)*10),
                                 ('C3','I-',include_low_3/(len(community_3)*4)*10),

                                 ('C1','DNI',not_include_1/(len(community_1)*4)*10),
                                 ('C2','DNI',not_include_2/(len(community_2)*4)*10),
                                 ('C3','DNI',not_include_3/(len(community_3)*4)*10),

                                 ('C1','NA',no_answer_1/(len(community_1)*4)*10),
                                 ('C2','NA',no_answer_2/(len(community_2)*4)*10),
                                 ('C3','NA',no_answer_3/(len(community_3)*4)*10)

                                 ])

top = nx.bipartite.sets(Group_B)[0]
pos = nx.bipartite_layout(Group_B, top)

pos['C1'] = (0, 1)

pos['C2'] = (0, 0)

pos['C3'] = (0, -1)




pos['I+'] = (1, 1)

pos['I-'] = (1, 0)

pos['DNI'] = (1, -1)

pos['NA'] = (1, -2)


edges = Group_B.edges()
weights = [Group_B[u][v]['weight'] for u,v in edges]

nx.draw(Group_B, pos=pos,
        #node_size=1000, 
        with_labels=True,
        width=weights,
        
         )

from networkx import *

nodes = nx.draw_networkx_nodes(Group_B, pos=pos, 
                               node_size=650,
                               node_color = 'white',
                               edgecolors = 'black')


nx.draw_networkx_edge_labels(Group_B,pos,edge_labels={
    ('C1','I+'):include_high_1,
    ('C2','I+'):include_high_2,
    ('C3','I+'):include_high_3,

    ('C1','I-'):include_low_1,
    ('C2','I-'):include_low_2,
    ('C3','I-'):include_low_3,

    ('C1','DNI'):not_include_1,
    ('C2','DNI'):not_include_2,
    ('C3','DNI'):not_include_3,

    ('C1','NA'):no_answer_1,
    ('C2','NA'):no_answer_2,
    ('C3','NA'):no_answer_3,

    
    },
    font_color='black',
    label_pos=0.2)

plt.savefig('MEDI_IMD_Group_B.pdf', format='pdf',bbox_inches='tight',transparent=True)
plt.show()





