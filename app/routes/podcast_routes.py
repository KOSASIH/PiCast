from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService

podcast_blueprint = Blueprint('podcast', __name__)

@podcast_blueprint.route('/podcasts', methods=['GET'])
def get_podcasts():
    podcasts = PodcastService.get_all_podcasts()
    return jsonify([podcast.to_dict() for podcast in podcasts])

@podcast_blueprint.route('/podcasts/<int:podcast_id>', methods=['GET'])
def get_podcast(podcast_id):
    podcast = PodcastService.get_podcast_by_id(podcast_id)
    return jsonify(podcast.to_dict())
