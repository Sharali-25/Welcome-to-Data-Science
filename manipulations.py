import pandas as pd
data={
    "id": [1,2,3,4],
    "name": ["Sharali","Sharol","Yeyleen","Vivian"],
    "role": ["CEO",None,None,None],
    "Salary": [200,100,None,None]
}
df=pd.DataFrame(data)
print("Original Data frame\n")
print(df)

print("\nfirst two rows:\n")
print(df.head(2))

print("\nlast two rows:\n")
print(df.tail(2))

print("\nTotal null values:\n")
print(df.isnull().sum())

print("\nData frame info:\n")
print(df.info())

new_df1= df.dropna()
print(new_df1)

new_df2= df.dropna(axis=1)
print(new_df2)

df["Salary"]=df["Salary"].fillna(300)
print(df)

df["role"]=df["role"].fillna("CEO")
print(df)