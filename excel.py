import pandas as pd

data = {
    "Name": ["Tony", "Robert", "John", "Alice"],
    "Age": [18, 24, 19, 21]
}

df = pd.DataFrame(data)

print(df)

writer = pd.ExcelWriter("test.xlsx", engine="xlsxwriter")
df.to_excel(writer, index=False)
writer.close()
