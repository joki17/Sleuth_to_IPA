import os
import pandas as pd


masterfile = []
#name of output file 
result_file = "oneGene_forIPA.csv"

#open file with results of genes from differential RNA seq analysis
with open('GH_list_forIPA.txt') as f:
    table = pd.read_table(f, sep="\t", index_col=None, header=None)

print (table.shape)

#get df with only column 0, ext gene name
df1 = table.iloc[:,0]

array = []
count_array = []

#count starts at -1, to match df numbering
count = -1
for item in df1:
	count += 1

	if item not in array:
		array.append(item)
		count_array.append(count)
	
df2 = table.iloc[count_array,:]
print (df2)

with open(result_file,'w') as csvfile:
    df2.to_csv(result_file, sep=',')






