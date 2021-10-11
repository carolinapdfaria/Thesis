#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:52:18 2021

@author: carolinafaria
"""

# This file concerns the construction of the complex network, the use of a 
# community detection algorithm and the visualisation and analysis of results.

# This file concerns the MEDI-VALUE project, more specifically the 
# implantable medical devices survey. In this case, both agreement and 
# conflict are considered.


# 3. Conversion of the vector-based data set into network-based data

# Library for network construction and visualisation
import networkx as nx
# Library for manipulating .csv files
import csv
# Library for visualisation and plots
import matplotlib.pyplot as plt


# For the labels and titles font
csfont = {'fontname':'Arial'}

# All available files. This list does not present the complete name of the 
# files, only the necessary part for later automatic uses.
original_files = ['type_AA','type_BB','type_CC','type_DD','type_EE','type_FF','type_GG',
         'type_HH','type_II',
         'all_items',
         'item_01','item_02','item_03','item_04','item_05','item_06','item_07',
         'item_08','item_09','item_10','item_11','item_12','item_13','item_14',
         'item_15','item_16','item_17','item_18','item_19','item_20','item_21',
         'item_22','item_23','item_24','item_25','item_26','item_27','item_28',
         'item_29','item_30','item_31','item_32','item_33','item_34']



for file in original_files:


    if file[0:4] == 'item':
        thresholds = [0]
    else:
        thresholds = [0.4,0.5,0.6,0.7,0.8]
        
    for threshold in thresholds:

        threshold = str(threshold)
        
        # I. Import original pre-processed data in order to have node information

        # Open the .csv file with the aswers 
        with open(file[0:3]+'/'+file[-2:]+'/'+file+'.csv', 'r') as nodecsv: 
        # read the .csv file
            nodereader = csv.reader(nodecsv, delimiter=';')  
            nodes = [n for n in nodereader][1:]

        # List of the nodes' names
        node_names = [n[0] for n in nodes] 

        # Create the graph G
        G = nx.Graph()
    
        # Add the nodes to the graph
        G.add_nodes_from(node_names)

        # Create an empty dictionary for each attribute
        stakeholder_dict = {}

        # Loop through the list, one row at a time
        for node in nodes: 
            # Access the correct item, add it to the corresponding dictionary
            stakeholder_dict[node[0]] = node[1]
    
    
        # Add the stakeholder group attribute
        nx.set_node_attributes(G, stakeholder_dict, 'stakeholder_group')





        # II. Import edges (originated from the implementation in write_edges.py files)
        

        # Open the .csv file with the edges information [created before]
        with open(file[0:3]+'/'+file[-2:]+'/Edges_'+file+'_'+str(threshold)+'.csv', 'r') as edgecsv: # Open the file
    
            # Read the .csv file
            edgereader = csv.reader(edgecsv) 
            # Retrieve the data
            edges = [tuple(e) for e in edgereader][1::] 
    
    
        # Add edges to the graph
        G.add_weighted_edges_from(edges)

        # The attribute "weight" is converted into float
        for u,v,d in G.edges(data=True):
            d['weight'] = float(d['weight'])
    
    
        # (5.) Visualisation and analysis - complete network
    
    
        # I. Save general information about the graph

        txt_file_general = open(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/results_'+file+'_'+threshold+'.txt', 'w') 

        writer_general = csv.writer(txt_file_general,delimiter=' ')
        writer_general.writerow([nx.info(G)])
        writer_general.writerow(['Density:'+ str(nx.density(G))])
        writer_general.writerow([' '])
            

        # II. Plot the network

        # create empty list for node colors
        node_color = []

        # Lists of the nodes of each stakeholder group
        # This will be needed in order for the node color to change according to the group
        Buyers_nodes = []
        HCPro_nodes = []
        PC_nodes = []
        Industry_nodes = []





        # Loop for each node in the graph in order to fill the groups node lists
        for node in G.nodes(data=True):
            if 'Healthcare professionals (doctors, nurses, pharmacists, technicians)' in node[1]['stakeholder_group']:
                HCPro_nodes.append(node[0])

            elif 'Buyers, policymakers and academics' in node[1]['stakeholder_group']:
                Buyers_nodes.append(node[0])

            elif 'Patients and citizens' in node[1]['stakeholder_group']:
                PC_nodes.append(node[0])

            elif 'Industry' in node[1]['stakeholder_group']:
                Industry_nodes.append(node[0])
        
        


        # Define position of nodes
        pos = nx.spring_layout(G, k=0.9)  


        # Draw the nodes of each group. This way, they get different colors
        nx.draw_networkx_nodes(G, node_size=15, pos=pos, nodelist=HCPro_nodes,
                               node_color='gold', label='Healthcare Professionals')

        nx.draw_networkx_nodes(G, node_size=15, pos=pos, nodelist=Buyers_nodes,
                               node_color='hotpink', label='Buyers, policymakers and academics')

        nx.draw_networkx_nodes(G, node_size=15, pos=pos, nodelist=PC_nodes,
                               node_color='palegreen', label='Patients and citizens')

        nx.draw_networkx_nodes(G, node_size=15, pos=pos, nodelist=Industry_nodes,
                               node_color='deepskyblue', label='Industry')




        nx.draw_networkx_edges(G, pos=pos, width = 0.1)


        import matplotlib.font_manager as font_manager

        font = font_manager.FontProperties(family='Arial', style='normal', size=10)


        plt.axis('off')
        plt.legend(bbox_to_anchor=(1.2,0), loc="lower right", 
                   bbox_transform=plt.gcf().transFigure, prop=font)


        plt.title('MEDI-VALUE - Network, Threshold = '+ threshold,**csfont)

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/full_network_'+file+'_'+threshold+'.pdf', format='pdf',bbox_inches='tight')

        plt.show()







        # III. Evaluate degree and degree distribution

        # Needed libraries for the histrogram representation
        import collections
        from matplotlib.ticker import FormatStrFormatter

        # Degree of each node
        degree_normal = G.degree()

        # Degree of each node taking weight into consideration
        degree_weighted = G.degree(weight='weight')


        # Calulate degree distribution, for all stakeholders and per group / type

        # All stakeholders 

        # NOT WEIGHTED
        degree_sequence_all = sorted([d for n, d in degree_normal], reverse=True) 
        degreeCount_all = collections.Counter(degree_sequence_all )
        deg_all, cnt_all = zip(*degreeCount_all.items())
        
        fig, ax = plt.subplots()

        plt.bar(deg_all, cnt_all, align='center', width=0.7, color="orange")

        plt.title("Degree Distribution - All Stakeholders ",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d  for d in deg_all])
        ax.set_xticklabels(deg_all,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/degree_distribution_all_stakeholders.pdf', format='pdf')
        plt.show()

        # WEIGHTED
        degree_sequence_weighted = sorted([d for n, d in degree_normal], reverse=True)  # degree sequence
        degreeCount_weighted = collections.Counter(degree_sequence_weighted )
        deg_weighted, cnt_weighted = zip(*degreeCount_weighted.items())

        fig, ax = plt.subplots()
        plt.bar(deg_weighted, cnt_weighted, align='center', width=0.70, color="orange")

        plt.title("Weighted Degree Distribution - All Stakeholders ",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_weighted])
        ax.set_xticklabels(deg_weighted,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/weighted_degree_distribution_all_stakeholders.pdf', format='pdf')
        plt.show()


        # Degree per type

        # NOT WEIGHTED

        # HC PROFESSIONALS
        degree_sequence_HCP = sorted([d for n, d in G.degree(HCPro_nodes)], reverse=True)  # degree sequence
        degreeCount_HCP = collections.Counter(degree_sequence_HCP)
        deg_HCP, cnt_HCP = zip(*degreeCount_HCP.items())

        fig, ax = plt.subplots()
        plt.bar(deg_HCP, cnt_HCP, width=0.70, color="orange", align='center')

        plt.title("Degree Distribution - Healthcare Professionals",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_HCP])
        ax.set_xticklabels(deg_HCP,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/degree_distribution_HC_Pro.pdf', format='pdf')
        plt.show()



        # PC 
        degree_sequence_PC = sorted([d for n, d in G.degree(PC_nodes)], reverse=True)  # degree sequence
        degreeCount_PC = collections.Counter(degree_sequence_PC)
        deg_PC, cnt_PC = zip(*degreeCount_PC.items())

        fig, ax = plt.subplots()
        plt.bar(deg_PC, cnt_PC,width=0.70, color="orange", align='center')

        plt.title("Degree Distribution - Patients and citizens",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_PC])
        ax.set_xticklabels(deg_PC,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/degree_distribution_PC.pdf', format='pdf')
        plt.show()
        

        # Industry 
        degree_sequence_Industry = sorted([d for n, d in G.degree(Industry_nodes)], reverse=True)  # degree sequence
        degreeCount_Industry = collections.Counter(degree_sequence_Industry)
        deg_Industry, cnt_Industry = zip(*degreeCount_Industry.items())

        fig, ax = plt.subplots()
        plt.bar(deg_Industry, cnt_Industry, width=0.70, color="orange", align='center')

        plt.title("Degree Distribution - Industry",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_Industry])
        ax.set_xticklabels(deg_Industry,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/degree_distribution_Industry.pdf', format='pdf')
        plt.show()

        # Buyers
        degree_sequence_Buyers = sorted([d for n, d in G.degree(Buyers_nodes)], reverse=True)  # degree sequence
        degreeCount_Buyers = collections.Counter(degree_sequence_Buyers)
        deg_Buyers, cnt_Buyers = zip(*degreeCount_Buyers.items())

        fig, ax = plt.subplots()
        plt.bar(deg_Buyers, cnt_Buyers, width=0.70, color="orange", align='center')

        plt.title("Degree Distribution - Buyers, policymakers and academics",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_Buyers])
        ax.set_xticklabels(deg_Buyers,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/degree_distribution_Buyers.pdf', format='pdf')
        plt.show()





        # WEIGHTED 

        # HC Professionals
        degree_sequence_HCP = sorted([d for n, d in G.degree(HCPro_nodes,weight='weight')], reverse=True)  # degree sequence
        degreeCount_HCP = collections.Counter(degree_sequence_HCP)
        deg_HCP, cnt_HCP = zip(*degreeCount_HCP.items())

        fig, ax = plt.subplots()
        plt.bar(deg_HCP, cnt_HCP, width=0.70, color="orange", align='center')

        plt.title("Weighted Degree Distribution - Healthcare Professionals",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_HCP])
        ax.set_xticklabels(deg_HCP,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/weighted_degree_distribution_HC_Pro.pdf', format='pdf')
        plt.show()



        # PC 
        degree_sequence_PC = sorted([d for n, d in G.degree(PC_nodes,weight='weight')], reverse=True)  # degree sequence
        degreeCount_PC = collections.Counter(degree_sequence_PC)
        deg_PC, cnt_PC = zip(*degreeCount_PC.items())

        fig, ax = plt.subplots()
        plt.bar(deg_PC, cnt_PC, width=0.70, color="orange", align='center')
        
        plt.title("Weighted Degree Distribution - Patients and citizens",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_PC])
        ax.set_xticklabels(deg_PC,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/weighted_degree_distribution_PC.pdf', format='pdf')
        plt.show()
        

        # Industry 
        degree_sequence_Industry = sorted([d for n, d in G.degree(Industry_nodes,weight='weight')], reverse=True)  # degree sequence
        degreeCount_Industry = collections.Counter(degree_sequence_Industry)
        deg_Industry, cnt_Industry = zip(*degreeCount_Industry.items())

        fig, ax = plt.subplots()
        plt.bar(deg_Industry, cnt_Industry, width=0.70, color="orange", align='center')

        plt.title("Weighted Degree Distribution - Industry",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_Industry])
        ax.set_xticklabels(deg_Industry,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/weighted_degree_distribution_Industry.pdf', format='pdf')
        plt.show()

        # Buyers
        degree_sequence_Buyers = sorted([d for n, d in G.degree(Buyers_nodes,weight='weight')], reverse=True)  # degree sequence
        degreeCount_Buyers = collections.Counter(degree_sequence_Buyers)
        deg_Buyers, cnt_Buyers = zip(*degreeCount_Buyers.items())

        fig, ax = plt.subplots()
        plt.bar(deg_Buyers, cnt_Buyers, width=0.70, color="orange", align='center')

        plt.title("Weighted Degree Distribution - Buyers, policymakers and academics",**csfont)
        plt.ylabel("Frequency",**csfont)
        plt.xlabel("Degree",**csfont)
        if file[0:4] == 'item':
            ax.set_xlim(0, 153) # for the bar not to cover everything
        ax.set_xticks([d for d in deg_Buyers])
        ax.set_xticklabels(deg_Buyers,fontsize=5,**csfont,ha='center', rotation = 60)
        ax.yaxis.set_tick_params(labelsize='xx-small')
        ax.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/weighted_degree_distribution_Buyers.pdf', format='pdf')
        plt.show()

        



        # IV. Other metrics and measurements of the network

        triadic_closure = nx.transitivity(G)

        writer_general.writerow(["Triadic closure:", triadic_closure])
        writer_general.writerow([' '])


        writer_general.writerow(['Attribute Assortativity Coeff: ', nx.attribute_assortativity_coefficient(G,'stakeholder_group' )])
        writer_general.writerow([' '])

        writer_general.writerow(['Average neighbor degree of each node:', nx.average_neighbor_degree(G)])
        writer_general.writerow([' '])

        writer_general.writerow(['Average degree connectivity:', nx.average_degree_connectivity(G)])
        writer_general.writerow([' '])

        writer_general.writerow(['K-nearest neigbours:', nx.k_nearest_neighbors(G)])
        writer_general.writerow([' '])

        writer_general.writerow(['Attribute_mixing_matrix:', nx.attribute_mixing_matrix(G,'stakeholder_group')])
        writer_general.writerow([' '])

        


        # 4. Using Louvain CD algorithm to find communities


        # Library for the implementation of the Louvain CD Algorithm
        import community as community_louvain
        
        # Find best partition using the Louvain Algorithm
        partition = community_louvain.best_partition(G,randomize=False, random_state=None)


        writer_general.writerow(['Partition modularity:',community_louvain.modularity(partition, G)])
        writer_general.writerow([' '])


        partitions_items = partition.items()


        txt_file_communities_detail = open(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/results_communities_'+file+'_'+threshold+'.txt', 'w') 

        writer_detail = csv.writer(txt_file_communities_detail,delimiter=' ')

        writer_detail.writerow(['Partition items', partitions_items])
        writer_detail.writerow([' '])



        # available partitions
        partitions_set = set(partition.values())
        number_of_partitions = len(partitions_set)

        # list of ordered partitions
        partitions_for_each = partition.values()

        def getList(dict):
            return dict.keys()

        all_partitions_nodes = getList(partition)


        nodes_partition = nodes


        partitions_for_each_list = list(partition.values())

        for i in range (0, len(nodes_partition)):
            nodes_partition[i].append(partitions_for_each_list[i])
    


        writer_general.writerow(['Number of communities:',number_of_partitions])
        writer_general.writerow([' '])

        





        # (5.) Visualisation and analysis - communities

        # I. Plots of communities
        import matplotlib.cm as cm
        
        # Define nodes position
        pos = nx.spring_layout(G, k=0.9)


        # Color of the nodes according to their partition
        cmap = cm.get_cmap('viridis', max(partition.values()) + 1)

        for node in partition.items():
            nx.draw_networkx_nodes(G, pos, partition.keys(), node_size=14, 
                                   cmap=cmap, node_color=list(partition.values()))


        nx.draw_networkx_edges(G, pos, alpha=0.5, width=0.1)

        plt.title('MEDI-VALUE -Communities, Threshold = '+ threshold,**csfont)
        plt.axis('off')

        plt.savefig(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/community_network_'+file+'_'+threshold+'.pdf', format='pdf',bbox_inches='tight')
        
        plt.show()





        # II. Evaluation of each partition

        # Size of each partition
        # Group of answers distribution per partition

        writer_detail.writerow([' '])

        if file[0:4] == 'item':
            for n in range (0, number_of_partitions):
                size=0
                number_critic_fund = 0
                number_complementary = 0
                number_irrelevant = 0
                number_none = 0
                for i in range (0, len(nodes_partition)):
                    if nodes_partition[i][-1] == n:
                        size+=1
                        if nodes_partition[i][2] == "Don't know / Don't want to answer":
                            number_none += 1
                            
                        elif nodes_partition[i][2] == "Complementary":
                            number_complementary += 1
                            
                        elif nodes_partition[i][2] == "Critical" or nodes_partition[i][2] == "Fundamental":
                            number_critic_fund += 1
                            
                        elif (nodes_partition[i][2] == 'Irrelevant'):
                            number_irrelevant += 1
                           
                    
                perc_critic_fund = number_critic_fund/size *100
                perc_complementary = number_complementary/size *100
                perc_irrelevant = number_irrelevant/size *100
                perc_none = number_none/size *100
                


                writer_general.writerow(['Community{} has {} elements'.format(n,size)])
                writer_detail.writerow(['Community{} has {} elements'.format(n,size)])
                writer_general.writerow(['Community{} has {} critical or fundamental ({}%), {} complementary ({}%), {} irrelevant ({}%) and {} none responses ({}%)'.format(n,number_critic_fund, perc_critic_fund, number_complementary, perc_complementary,number_irrelevant, perc_irrelevant, number_none, perc_none)])



        # If we are evaluating more than one item it is not usefull to know the distribution
        # of answers.
        else:
            print ('More than one item.')
            for n in range (0, number_of_partitions):
                size=0
                for i in range (0, len(nodes_partition)):
                    if nodes_partition[i][-1] == n:
                        size+=1
           
                writer_general.writerow(['Community{} has {} elements'.format(n,size)])


        writer_detail.writerow([' '])
        writer_general.writerow([' '])


        # Evaluate distribution of stakeholder type per partition
        
        stakeholder_type = ['Healthcare professionals (doctors, nurses, pharmacists, technicians)',
                            'Patients and citizens',
                            'Industry',
                            'Buyers, policymakers and academics']

        for n in range (0, number_of_partitions):
            size=0

            number_HPro = 0
            number_PC = 0
            number_Industry = 0
            number_Buyers = 0

            for i in range (0, len(nodes_partition)):
                # if nodes_partition[i][2+number of items being considered] == n:
                if nodes_partition[i][-1] == n:
                    size+=1
                    if nodes_partition[i][1] == 'Healthcare professionals (doctors, nurses, pharmacists, technicians)':
                        number_HPro += 1
            
                
                    elif nodes_partition[i][1] == 'Patients and citizens':
                        number_PC += 1
                
                    elif nodes_partition[i][1] == 'Industry':
                        number_Industry += 1
                
                    elif nodes_partition[i][1] == 'Buyers, policymakers and academics':
                        number_Buyers += 1
                

                

            perc_HPro = number_HPro/size *100
            perc_PC = number_PC/size *100
            perc_Industry = number_Industry/size *100
            perc_Buyers = number_Buyers/size *100

                
                


            writer_detail.writerow(['Community{} has {} elements'.format(n,size)])
            writer_detail.writerow(['Community{} has {} HPro ({}%), {} Patiens & Citizens ({}%), {} Industry ({}%) and {} Payers ({}%)'.format(n,number_HPro, perc_HPro, number_PC, perc_PC,number_Industry, perc_Industry, number_Buyers, perc_Buyers)])
    
        writer_detail.writerow([' '])


        # For confirmation
        for s in stakeholder_type:
            size_type =0
    
            for i in range (0, len(nodes_partition)):
        
                if nodes_partition[i][1] == s:
            
                    size_type +=1         
            

            writer_general.writerow(['There are {} {} stakeholders'.format(size_type,s)])
            

        writer_general.writerow([' '])



        # III. Other measures related to clustering and communities


        clustering_coef = nx.clustering (G, weight = 'None')
        clustering_coef_weighted = nx.clustering (G,weight='weight')
        average_clustering_coef = nx.average_clustering(G,weight='None')
        average_clustering_coef_weighted = nx.average_clustering(G,weight='weight')
        
        writer_detail.writerow(['Clustering coeffiecient:', clustering_coef])
        writer_general.writerow([' '])
        
        writer_detail.writerow(['Clustering coeffiecient weighted:', clustering_coef_weighted])
        writer_general.writerow([' '])


        writer_general.writerow(['Average clustering coeffiecient:',average_clustering_coef])
        writer_general.writerow([' '])
        
        writer_general.writerow(['Average clustering coeffiecient weighted:',average_clustering_coef_weighted])
        writer_general.writerow([' '])


        # Calculate the number of intra-community edges for a partition of G.
        # The coverage of a partition is the ratio of the number of intra-community
        # edges to the total number of edges in the graph.


        txt_file_ratio = open(file[0:3]+'/'+file[-2:]+'/Results/'+threshold+'/results_ratio_'+file+'_'+threshold+'.txt', 'w') 

        writer_ratio = csv.writer(txt_file_ratio,delimiter=' ')


        total_intra_edges = 0
        total_inter_edges = 0
        for n in range (0, number_of_partitions):     
            number_intra_com_edges = 0  
            number_inter_com_edges = 0
            coverage = 0
            inter_com_edges = []
            intra_com_edges = []
    

            for i in range (0, len(edges)): 
                if partition[edges[i][0]] == n and partition[edges[i][1]] == n:
                    intra_com_edges.append([edges[i][0],edges[i][1]])
                    number_intra_com_edges +=1
                    total_intra_edges +=1
            
            
                elif (partition[edges[i][0]] == n and partition[edges[i][1]] != n) or (partition[edges[i][0]] != n and partition[edges[i][1]] == n):
                    inter_com_edges.append([edges[i][0],edges[i][1]])
                    number_inter_com_edges +=1
                    total_inter_edges +=1
           
            coverage = number_intra_com_edges / len(edges)
    
    

            writer_ratio.writerow(['Number of intra-community edges for community {}: {}'.format(n,number_intra_com_edges)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Number of inter-community edges for community {}: {}'.format(n,number_inter_com_edges)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Inter community edges for community {}: {}'.format(n,inter_com_edges)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Length of inter_com_edges:',len(inter_com_edges)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Intra community edges for community {}: {}'.format(n,intra_com_edges)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Length of intra_com_edges:',len(intra_com_edges)])
            writer_ratio.writerow([''])
    
            if number_intra_com_edges !=0 :
                writer_ratio.writerow(['Inter/Intra ratio of community {} : {}'.format( n,number_inter_com_edges/number_intra_com_edges)])
                writer_ratio.writerow([''])
   
            else:
                writer_ratio.writerow(['No ratio possible, the number of intra-community edges is zero'])
                writer_ratio.writerow([''])
    
            writer_ratio.writerow(['Coverage of community {} : {}'.format(n,coverage)])
            writer_ratio.writerow([''])
            writer_ratio.writerow(['Coverage (%) of community {} : {}%'.format(n,coverage*100)])
            writer_ratio.writerow([''])


        writer_ratio.writerow(['Total number of intra-community edges: {}'.format(total_intra_edges)])
        writer_ratio.writerow(['Total number of inter-community edges: {}'.format(total_inter_edges)])
        writer_ratio.writerow([''])




        txt_file_general.close()
        txt_file_communities_detail.close()
        txt_file_ratio.close()
        


    
    
    
    
    
    
    