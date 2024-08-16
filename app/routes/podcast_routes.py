from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from app.hybrid_recommendation import HybridRecommendation

podcast_blueprint = Blueprint('podcast', __name__)

hybrid_recommendation = HybridRecommendation(user_podcast_matrix, podcast_episodes)

@podcast_blueprint.route('/podcasts/recommendations/hybrid', methods=['GET'])
def get_hybrid_recommendations():
    user_id = request.args.get('user_id')
    podcast_id = request.args.get('podcast_id')
    recommendations = hybrid_recommendation.predict_recommendations(user_id, podcast_id)
    return jsonify({'recommendations': recommendations})
