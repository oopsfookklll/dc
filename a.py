import numpy as np
import pandas as pd
from tabulate import tabulate

# read input CSV file
filename = input('Enter input CSV filename: ')
df = pd.read_csv(filename)

# sum up Reference column and group by Patient name, Test name, and DC columns
df = df.groupby(['Patient name', 'Test name', 'DC']).agg({'Reference': 'sum'}).reset_index()

# count number of changes and sum of DC column for each group of rows with the same Reference and Test name values
counts = df.groupby(['Patient name', 'Test name', 'Reference']).agg({'DC': 'sum', 'Reference': 'size'})

# rename columns in counts DataFrame
counts = counts.rename(columns={'DC': 'DC Sum', 'Reference': 'Count'})

# reset index of counts DataFrame
counts = counts.reset_index()

# exclude rows with 'SELF' in the Reference column
counts = counts[counts['Reference'] != 'SELF']

# sort counts DataFrame by Reference column
counts = counts.sort_values('Reference')

# group by Reference and Test name columns and count number of unique Patient name values
counts['Count'] = counts.groupby(['Reference', 'Test name'])['Patient name'].transform('nunique')

# drop Patient name column
counts = counts.drop('Patient name', axis=1)

# define column colors using ANSI escape codes
column_colors = {'Test name': '\033[1;33m', 'Reference': '\033[1;34m', 'Count': '\033[1;32m', 'DC Sum': '\033[1;32m'}

# define color map based on Count column
color_map = pd.cut(counts['Count'], bins=[-np.inf, 1, 2, 3, 4, np.inf], labels=['#00FF00', '#33FF00', '#66FF00', '#99FF00', '#CCFF00'])

# format counts DataFrame as a table with borders and colors
table = tabulate(counts, headers='keys', tablefmt='html', showindex=False, numalign='center', stralign='center', colalign=['center', 'center', 'center'], disable_numparse=True)

# replace column names with colored column names
for col, color in column_colors.items():
    table = table.replace(col, color + col + '\033[0m')

# apply color map to Count column
table = table.replace(' #00FF00 ', ' <span class="count-1"> </span> ')
table = table.replace(' #33FF00 ', ' <span class="count-2"> </span> ')
table = table.replace(' #66FF00 ', ' <span class="count-3"> </span> ')
table = table.replace(' #99FF00 ', ' <span class="count-4"> </span> ')
table = table.replace(' #CCFF00 ', ' <span class="count-5"> </span> ')

# create HTML table from formatted table
html_table = '<table>' + table + '</table>'

# define CSS styles for Count column
css_styles = '''
<style>
.count-1 {
    color: #00FF00;
}
.count-2 {
    color: #33FF00;
}
.count-3 {
    color: #66FF00;
}
.count-4 {
    color: #99FF00;
}
.count-5 {
    color: #CCFF00;
}
</style>
'''

# prompt user for output filename
output_filename = input('Enter output HTML filename: ')

# add .html extension to output filename
if not output_filename.endswith('.html'):
    output_filename += '.html'

# write HTML table to file
with open(output_filename, 'w') as f:
    f.write(css_styles)
    f.write(html_table)
