import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

spotify_data = pd.read_csv("tracks_features.csv") # load dataset

features = ['explicit', 'danceability', 'energy', 'key', 'loudness', 'liveness', 'tempo'] # selected features for song comparision

scaler = MinMaxScaler()
spotify_data_normalized = scaler.fit_transform(spotify_data[features])

def find_similar_songs(input_song_name, song_df, scaler, features):
    input_song = song_df[song_df['name'] == input_song_name].iloc[0]
    input_features = input_song[features].values.reshape(1, -1)
    input_features_normalized = scaler.transform(input_features)
    
    similarity_scores = cosine_similarity(input_features_normalized, spotify_data_normalized) # calculate cosine similarity
    
    similar_songs_indices = similarity_scores.argsort()[0][::-1][1:11] # return top 10 scores
    similar_songs = [(song_df.iloc[i]['name'], similarity_scores[0][i]) for i in similar_songs_indices]
    return similar_songs

if __name__ == "__main__":
    input_song_name = "Despacito"
    similar_songs = find_similar_songs(input_song_name, spotify_data, scaler, features)
    print("Similar songs based on Cosine Similarity for:", input_song_name)
    for song in similar_songs:
        print(song)