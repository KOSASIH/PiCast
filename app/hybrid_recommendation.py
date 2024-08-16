# app/hybrid_recommendation.py
from app.recommendations import RecommendationModel
from app.content_based_filtering import ContentBasedFiltering

class HybridRecommendation:
    def __init__(self, user_podcast_matrix, podcast_episodes):
        self.recommendation_model = RecommendationModel(user_podcast_matrix)
        self.content_based_filtering = ContentBasedFiltering(podcast_episodes)

    def predict_recommendations(self, user_id, podcast_id):
        cf_recommendations = self.recommendation_model.predict_recommendations(user_id)
        cbf_recommendations = self.content_based_filtering.predict_recommendations(podcast_id)
        hybrid_recommendations = list(set(cf_recommendations) & set(cbf_recommendations))
        return hybrid_recommendations
