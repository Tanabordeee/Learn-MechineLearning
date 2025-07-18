import pandas as pd

df = pd.read_csv("sales_data_100.csv")
#print(df)
#print(df.head(5))
#print(df.info())
# print(df.loc[(df["Category"] == "Furniture") & (df["Price"] > 1000)])
# print(df.loc[df["OrderDate"] >= "2024-02-01"])
# print(df.isna())

print("HEAD" , df.head(10))
print("MAX" , df["Price"].max())
print("MEAN" , df["Price"].mean())
df["Total Price"] = df["Quantity"] * df["Price"]
#print(df.head())
d = []
for i in df["Category"]:
    if i == "IT":
        d.append(10)
    else:
        d.append(5)

df["Discount"] = d 
print("----------------------------")
print(df.head())
print("----------------------------")
df["NetPrice"] = (100 - df["Discount"])/100 * df["Total Price"]
print(df.head())
print("-----------------------")
print(df.groupby("Category")["Total Price"].sum())
print("-----------------------")
print(df.groupby("Region")["Quantity"].sum())
print("-------------------")
data = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(data.iloc[:5])
print("-------------------")
data2 = df.groupby("Product")["Quantity"].sum().sort_values()
print(data2.iloc[:5])
print("--------------------")
print(df.groupby("Product")["Quantity"].sum() < 5)
