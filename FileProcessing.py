# This is a Python script.
#import the pandas package
import pandas as pd

#read the JSON file and convert it to DataFrame
df1 = pd.read_json("file.json")
#print(df1)

#read the CSV file and convert it to DataFrame
df2 = pd.read_csv("file.csv")
#print(df2)

#Combine DF1 and DF2 contents to DF3
df3 = df1.append(df2, ignore_index=True)
#print(df3)

#remove duplicates and sort by Salary Desc
df4 = df3.drop_duplicates(keep='first').sort_values('salary', ascending=False)
#print(df4)

#writing the DF contents to CSV file.
df4.to_csv("final.csv", index=False)

print("Done creating a csv file!")
