import pandas as pd

# 1. Wczytaj dane z pliku Excela
file_path = 'file_name.xlsx'
sheet = 'sheet_name'
df = pd.read_excel(file_path, sheet_name=sheet)

# Dodaj kolumnę z rangą dla wartości w obrębie tego samego id
df['rank'] = df.groupby('id').cumcount() + 1

# Lista kolumn, które chcesz przekształcić
cols_to_pivot = ['', '', ''] #insert columns name here

# Tworzymy listę kolumn, które zostaną przekształcone
dfs_combined = []

# Iterujemy po maksymalnej wartości rank i po kolumnach, które chcemy przekształcić
max_rank = int(df['rank'].max())
for i in range(1, max_rank + 1):
    for col in cols_to_pivot:
        if col in df.columns:
            df_pivot = df[df['rank'] == i].pivot(index='id', columns='rank', values=col)
            df_pivot.columns = [f"{col}_{int(j)}" for j in df_pivot.columns]  # Konwersja na int usuwa ".0"
            dfs_combined.append(df_pivot)

df_result = pd.concat(dfs_combined, axis=1).reset_index()

# Zapisz przekształcone dane do nowego pliku Excela
output_path = 'transformed_data.xlsx'
df_result.to_excel(output_path, index=False)
