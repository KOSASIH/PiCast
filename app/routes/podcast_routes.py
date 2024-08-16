from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from ai_model.make_recommendations import make_recommendations

podcast_blueprint = Blueprint('podcast', __name__)

@podcast_blueprint.route('/podcasts/recommend', methods=['GET'])
def get_recommended_podcasts():
    user_id = request.args.get('user_id')
    num_recommendations = request.args.get('num_recommendations', 10)
    recommended_podcasts = make_recommendations(user_id, num_recommendations)
    return jsonify([PodcastService.get_podcast_by_id(podcast_id).to_dict() for podcast_id in recommended_podcasts])
