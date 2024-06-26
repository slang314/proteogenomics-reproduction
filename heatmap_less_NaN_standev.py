"""
Steven Lang
EN.605.662.81.FA23
Final Project Code - Heatmap
12.06.23
"""

import pandas as pd
import plotly.express as pe

file = '77_cancer_proteomes_CPTAC_itraq_standev.csv'

data_frame = pd.read_csv(file)

cols = data_frame.shape[1]

subset = data_frame.iloc[1:, 3:]

col_names = subset.columns

subset = subset.dropna(axis='rows')
print(subset.shape[0],subset.shape[1])

subset = subset.drop(subset[subset['stdev'] <= 1.5].index, axis='rows')
print(subset.shape[0],subset.shape[1])

newnames = ['BC' + str(i) for i in range(80)]

newnames.append('healthy1')
newnames.append('healthy2')
newnames.append('healthy3')

rename_dict = {old_name: new_name for old_name, new_name in zip(col_names, newnames)}
subset.rename(columns=rename_dict, inplace=True)

subset = subset.iloc[:,:-1]

fig = pe.imshow(subset.values,
                labels=dict(color='Value'),
                x=subset.columns,
                color_continuous_scale='Viridis')

fig.update_layout(
    title={'text':'Heatmap: Breast Cancer Proteomic Data. n=83 (80 breast cancer samples, 3 healthy). Values = Log_2 iTRAQ ratio.','font':{'size':24}},
    xaxis=dict(title='Sample Name'),
    yaxis=dict(title='Genes')
)


fig.show()
fig.write_html('heatmap.html')