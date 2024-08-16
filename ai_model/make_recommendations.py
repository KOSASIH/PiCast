# ai_model/make_recommendations.py
import numpy as np
from ai_model.recommendation_model import RecommendationModel

def make_recommendations(user_id, num_recommendations):
    # Load the trained model
    model = RecommendationModel.load('recommendation_model.h5')

    # Get the user's embedding
    user_embedding = model.user_embedding.predict(np.array([user_id]))

    # Get the podcast embeddings
    podcast_embeddings = model.podcast_embedding.predict(np.arange(num_podcasts))

    # Calculate the dot product of the user and podcast embeddings
    scores = np.dot(user_embedding, podcast_embeddings.T)

    # Get the top N recommended podcasts
    recommended_podcasts = np.argsort(-scores)[:num_recommendations]

    return recommended_podcasts
