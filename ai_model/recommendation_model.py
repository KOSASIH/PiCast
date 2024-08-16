# ai_model/recommendation_model.py
import tensorflow as tf
from tensorflow.keras.layers import Embedding, Dense, Dropout
from tensorflow.keras.models import Model

class RecommendationModel(Model):
    def __init__(self, num_users, num_podcasts, embedding_dim):
        super(RecommendationModel, self).__init__()
        self.user_embedding = Embedding(num_users, embedding_dim, input_length=1)
        self.podcast_embedding = Embedding(num_podcasts, embedding_dim, input_length=1)
        self.dense1 = Dense(64, activation='relu')
        self.dropout1 = Dropout(0.2)
        self.dense2 = Dense(32, activation='relu')
        self.dropout2 = Dropout(0.2)
        self.output_layer = Dense(num_podcasts, activation='softmax')

    def call(self, inputs):
        user_id, podcast_id = inputs
        user_embedding = self.user_embedding(user_id)
        podcast_embedding = self.podcast_embedding(podcast_id)
        x = tf.concat([user_embedding, podcast_embedding], axis=1)
        x = self.dense1(x)
        x = self.dropout1(x)
        x = self.dense2(x)
        x = self.dropout2(x)
        output = self.output_layer(x)
        return output
