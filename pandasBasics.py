import pandas as pd

#LOADING DATA
df = pd.read_csv("data.csv")#reading cvs and txt
# df_txt = pd.read_csv("data.txt", delimiter='\t')
# # we using delimeter because txt file has invisble frames,if i dont use delimeter output has to be like \t41\t42
# df_exel = pd.read_excel("data.xlsx")#reading only exel
#df means data frames
# print(df.head(5))#head is first datas
# print(df.tail(5))#tail is last datas


#Read Headers
# print(df.columns)#showing to column names

#Read Each Column
# print(df['Name'][0:5])
# print(df[['Name', 'Type 1', 'HP']][0:10])
# print(df.name)

#Read Each Row
# print(df.iloc[9])#specific row
# print(df.iloc[1:3])#specific rows
# for index, row in df.iterrows():#giving to us names
#     print(index, row['Name'])

# print(df.loc[df['Type 1'] == "Fire"])

#Read a specific location
# print(df.iloc[4,1])

#sorting and describing data
# print(df.describe)
# print(df.sort_values('Name'))
# print(df.sort_values('Name', ascending=False))#ascending is doing reverse
# print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))#one is true otherone is false

#Adding column
# df['Total'] = df['Attack'] + df['Defense'] # SAME
# df['Total'] = df.iloc[:, 4:9].sum(axis=1)  # SAME
# print(df.tail(5))

#Take out column
# df = df.drop(columns=["Total"])
# print(df.head(4))

#Moving columns 
#create list
# cols = list(df.columns)
#move it them
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]] # be careful look at the cols[-1] it in the orher bracket so it is a list
# print(df.head(5))

#Saving Data
#we are using read_csv to take data 
#now we using to_csv to update or save data
# df.to_csv('modified.cvs', index = False) if u want to dont save any column use 'column name = False'
# df.to_excel('modified.xlsx', index = False)
# df.to_csv('modified.txt', index = False, sep = 't\')# for txt files usin invis datas 

#Filtering Data
# print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])#if u use 'and' it does not work

#I can create a new data using this 
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['HP'] > 70)]#Specific data
# new_df = new_df.reset_index() # reseting all index for new data file

#Still filtering
# print(df.loc[df['Name'].str.contains('Mega')])
# print(df.loc[~df['Name'].str.contains('Mega')])
# import re # regex is a tring parameter package or something like that
# print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I,  regex = True)])# we are writing lovver case but still working because we are using regex

#Contidional Changes
# df.loc[df['Type 1'] == 'Fire', 'Type 1'] = 'Flamer'
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True
# print(df)
# df.loc[df['HP'] > 79, ['Generation','Legendary']] = ['Test 1', 'Test 2']
# df.loc[df['Type 1'] == 'Fire', 'Osman'] = True# we can create a colmn like that
# print(df)

#Aggregate Statistic(Groupby)
# print(df.groupby(['Type 1']).mean())
# print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False))#we are grouping type 1 
# print(df.groupby(['Type 1']).sum)#why we are summing here idk

#counting
# df['Count'] = 1 #create a count column
# print(df.groupby(['Type 1']).count()['Count'])#count

#READING REALY BIG FILES (LIKE 30 GB)
# for df in pd.read_csv("C:/Users/Zihni UYSAL/Desktop/pandas-master/pokemon_data.csv", chunksize=5):
#     print("CHUNK DF")
#     print(df)

#Also we using like this
# new_df = pd.DataFrame(columns=df.columns)
# for df in pd.read_csv("C:/Users/Zihni UYSAL/Desktop/pandas-master/pokemon_data.csv", chunksize=5):
#     result = df.groupby(['Type 1']).count()

#     new_df = pd.concat([new_df, result]) #concat is adding a data,old one to new one
# print(new_df)