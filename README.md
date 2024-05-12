# Spotify Recommender

Command-line tool recommending a group of 5-10 songs to users given an input song. Utilizes 3 different ML algorithms to come
up with recommendations.

Group 2: Manvendra Chavan and Pawan Sarma

## Quick start

1. Install necessary Python libraries using pip
    - `pip install pandas scikit-learn numpy`

2. Run Cosine similarity:
    - `make run-cosine`
    - Enter an input song that exists in the dataset (examples: Happy, Despacito, Gangnam Style)

3. Run K-means:
    - `make k-means`
    - Enter an input song that exists in the dataset

4. Run KNN:
    - `make knn`
    - Enter an input song that exists in the dataset

## Dataset

Spotify 1.2M+ songs: https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs
- 1.2 millions songs from Spotify (345 MB)
- Contains variety of metadata per song (ex: danceability, energy, key, tempo, explicitness)
- Metadata derived from audio analysis algorithms from Spotify

**Note: Dataset included in this repository only contains 10K rows for testing purposes.**

## ML algorithms used

1. KNN:
2. K-Means:
3. Cosine similarity: Select feature comparision for input with each song in dataset. Cosine similiarty calculate the most minimal total difference one vector has from the other in each of its values.
