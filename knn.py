# -*- coding: utf-8 -*-
"""KNN

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z-ITpbD1BNgjnYgIUNNDA9t5d-7ANHRi
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

# Load and prepare your dataset
data_path = 'dataset.csv'
data = pd.read_csv(data_path)

# Preprocessing artist names if they are in list format
data['artists'] = data['artists'].apply(eval)

# Converting list of artists to a sorted, joined string for uniformity
data['artist_str'] = data['artists'].apply(lambda x: ', '.join(sorted(x)))

# Selecting the relevant features for the model
features = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']
X = data[features]

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Build the K-NN model
model_knn = NearestNeighbors(n_neighbors=11, algorithm='auto', metric='cosine')
model_knn.fit(X_scaled)

def get_recommendations(song_id, num_recommendations=10):
    # Find the index of the song
    song_index = data[data['id'] == song_id].index[0]

    # Retrieve the song's features
    song_features = X_scaled[song_index].reshape(1, -1)

    # Finding the nearest neighbors
    distances, indices = model_knn.kneighbors(song_features, n_neighbors=num_recommendations + 20)  # Increased number to filter out duplicates

    # Fetch the recommended song details
    recommendations = data.iloc[indices[0][1:]]

    # Remove duplicates based on 'name' and 'artist_str'
    unique_recommendations = recommendations.drop_duplicates(subset=['name', 'artist_str'])

    # If more than num_recommendations are found, cut down to the requested number
    if len(unique_recommendations) > num_recommendations:
        unique_recommendations = unique_recommendations.head(num_recommendations)

    return unique_recommendations

# Example
song_id = '54TSw5CeLFZu15srfUyWZ8'
recommendations = get_recommendations(song_id)

print("Recommendations for the input song:")
display(recommendations[['id', 'name', 'artists']])

display(recommendations[['id', 'name', 'artists']])
