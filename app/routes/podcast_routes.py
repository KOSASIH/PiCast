from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from app.content_based_filtering import ContentBasedFiltering

podcast_blueprint = Blueprint('podcast', __name__)

content_based_filtering = ContentBasedFiltering(podcast_episodes)

@podcast_blueprint.route('/podcasts/recommendations/content-based', methods=['GET'])
def get_content_based_recommendations():
    podcast_id = request.args.get('podcast_id')
    recommendations = content_based_filtering.predict_recommendations(podcast_id)
    return jsonify({'recommendations': recommendations})
