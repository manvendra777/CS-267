import pandas as pd
import time

start_time = time.time()

df = pd.read_csv("tracks_features.csv")

data_dict = df.to_dict(orient="records")

end_time = time.time()
elapsed_time = end_time - start_time

print("Time taken to read CSV and convert to dictionary: {:.4f} seconds".format(elapsed_time))

first_row = data_dict[0]
print(first_row)
