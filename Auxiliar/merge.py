import pandas as pd
import os

current_directory = os.path.dirname(os.path.abspath(__file__))

anime_csv_path = os.path.join(current_directory, 'animelist.csv')
anime_data = pd.read_csv(anime_csv_path)

extra_csv_path = os.path.join(current_directory, 'extra_data.csv')
extra_data = pd.read_csv(extra_csv_path)

merged_data = pd.merge(anime_data, extra_data, left_on='series_title', right_on='Name', how='left')

merged_data.drop('Name', axis=1, inplace=True)

output_csv_path = os.path.join(current_directory, 'merged_anime_data.csv')
merged_data.to_csv(output_csv_path, index=False)

print(f"CSV combinado foi gerado com sucesso! Local: {output_csv_path}")