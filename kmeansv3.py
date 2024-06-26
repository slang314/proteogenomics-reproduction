"""
Steven Lang
12.6.23
Final Project Code - PCA and Kmeans clustering
Data Visualization EN.605.662.81.FA23
"""

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as pe
import csv
import re

data = pd.read_csv('kmeans_final.csv', index_col='sample_orig.cluster_status')

km = KMeans(n_clusters=3, random_state=13).fit(data)

pca = PCA(n_components=2)
data_pca = pca.fit_transform(data)

clusters = pd.DataFrame()
clusters['data_index'] = data.index.values
clusters['cluster'] = km.labels_ + 1


rename_merge = pd.DataFrame(data_pca, columns=['pc1', 'pc2'])
rename_merge['Cluster'] = clusters['cluster']
rename_merge['Data_Index'] = data.index

names_out = rename_merge.iloc[:,-2:]

names_out.to_csv('clusters.csv', index=False)

with open('clusters.csv','r') as f:
    readin = csv.reader(f, delimiter=',')
    
    matches = 0
    mismatches = 0

    for line in readin:
        
        newcluster = line[0]
        longname = line[1]
        
        pat = r"_\d+_"

        if newcluster == 'Cluster':
            continue
        oldcluster = re.findall(pat,longname)
        oldcluster = str(oldcluster[0]).strip('_').split('_')
        oldcluster = oldcluster[0]

        if newcluster == oldcluster:
            matches += 1
        else:
            mismatches += 1

    total = matches + mismatches

    match_perc = matches / total * 100
    
    match_perc = round(match_perc,2)


fig = pe.scatter(rename_merge, x='pc1', y='pc2', color='Cluster', title=f'PCA Plot of KMeans Clustering. Match Percentage: {match_perc}%',
            hover_data={'Data_Index': True})

fig.update_xaxes(title_text='Principal Component 1')
fig.update_yaxes(title_text='Principal Component 2')

fig.add_annotation(text='   Hover Data: Data Index: Sample Name, Original Cluster, PAM50 Cancer Subtype',
                   x=0, y=0.98,
                   xref='paper', yref='paper',
                   xanchor='left', yanchor='bottom',
                   font=dict(size=12))

fig.add_annotation(text='   Note that the Data are largely reproduced from the original paper.',
                   x=0, y=0.95,
                   xref='paper', yref='paper',
                   xanchor='left', yanchor='bottom',
                   font=dict(size=12))


fig.update_traces(marker=dict(size=10))
fig.show()
