# app/recommendations.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense

class RecommendationModel:
    def __init__(self, user_podcast_matrix):
        self.user_podcast_matrix = user_podcast_matrix
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(Embedding(input_dim=self.user_podcast_matrix.shape[1], output_dim=128, input_length=self.user_podcast_matrix.shape[0]))
        model.add(Dense(64, activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        return model

    def train_model(self):
        self.model.fit(self.user_podcast_matrix, epochs=10, batch_size=32, verbose=2)

    def predict_recommendations(self, user_id):
        user_vector = self.user_podcast_matrix[user_id]
        scores = cosine_similarity(user_vector, self.user_podcast_matrix)
        top_scores = scores.argsort()[:-5:-1]
        return top_scores
