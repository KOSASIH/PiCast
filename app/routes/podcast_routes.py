from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from app.recommendations import RecommendationModel

podcast_blueprint = Blueprint('podcast', __name__)

recommendation_model = RecommendationModel(user_podcast_matrix)

@podcast_blueprint.route('/podcasts/recommendations', methods=['GET'])
def get_recommendations():
    user_id = request.args.get('user_id')
    recommendations = recommendation_model.predict_recommendations(user_id)
    return jsonify({'recommendations': recommendations})
