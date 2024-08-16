# app/user_podcast_matrix.py
import pandas as pd

def create_user_podcast_matrix():
    user_podcast_data = pd.read_csv('user_podcast_data.csv')
    user_podcast_matrix = user_podcast_data.pivot(index='user_id', columns='podcast_id', values='listen_count')
    return user_podcast_matrix

user_podcast_matrix = create_user_podcast_matrix()
