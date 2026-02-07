import pandas

df = pandas.read_csv("Squirrel_Data.csv")  # <-- your input file name
print(df)

# count each color (skip empty cells)
counts = df["Primary Fur Color"].dropna().value_counts()
print(counts)

# make it a nice 2-column table and save
color_count_df = counts.rename_axis("Primary Fur Color").reset_index(name="Count")
color_count_df.to_csv("squirrel_color_count.csv", index=False)

print(color_count_df)