from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from app.metrics import PodcastMetrics

podcast_blueprint = Blueprint('podcast', __name__)

metrics = PodcastMetrics()

@podcast_blueprint.route('/podcasts/<int:podcast_id>/play', methods=['GET'])
def play_podcast(podcast_id):
    metrics.increment_podcast_plays()
    # Play the podcast
    return jsonify({'message': 'Podcast played successfully'})

@podcast_blueprint.route('/podcasts/<int:podcast_id>/download', methods=['GET'])
def download_podcast(podcast_id):
    metrics.increment_podcast_downloads()
    # Download the podcast
    return jsonify({'message': 'Podcast downloaded successfully'})

@podcast_blueprint.route('/metrics', methods=['GET'])
def get_metrics():
    return metrics.podcast_plays, metrics.podcast_downloads, metrics.user_engagement
