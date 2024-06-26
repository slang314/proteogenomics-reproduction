"""
Steven Lang
12.06.23
Final Project Visual: Volcano Plot
EN.605.662.81.FA23
"""


import pandas as pd
import plotly.express as pe

file = 'modified_names_droppednas.csv'
data_frame = pd.read_csv(file)
subdf = data_frame.filter(['gene_name','foldchange','neglogpval'])

changes = data_frame.filter(['foldchange'])
#print(changes.head)

underexpressed = 0
overexpressed = 0

for index, value in changes.iterrows():
    if int(value) < 0:
        underexpressed += 1
    else:
        overexpressed += 1

#print(changes.shape[0])

fig = pe.scatter(subdf,x='foldchange',y='neglogpval', hover_data='gene_name',color='foldchange',title=f'Volcano Plot: {changes.shape[0]} Proteins, Cancer vs. Normal. Underexpressed: {underexpressed}, Overexpressed: {overexpressed}')
fig.update_xaxes(title_text='Fold Change (breast cancer sample protein expression minus control protein expression)')
fig.update_yaxes(title_text='-log_2 p-value (students 2-tailed t-test type 2)')
fig.show()
fig.write_html('volcano.html')