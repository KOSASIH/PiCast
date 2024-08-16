from flask import Blueprint, request, jsonify
from app.services.podcast_service import PodcastService
from moderation.moderation_service import ModerationService

podcast_blueprint = Blueprint('podcast', __name__)

@podcast_blueprint.route('/podcasts/<int:podcast_id>/report', methods=['POST'])
def report_podcast(podcast_id):
    user_id = request.json.get('user_id')
    reason = request.json.get('reason')
    description = request.json.get('description')
    ModerationService().report_podcast(podcast_id, user_id, reason, description)
    return jsonify({'message': 'Report submitted successfully'})

@podcast_blueprint.route('/podcasts/<int:podcast_id>/moderate', methods=['POST'])
def moderate_podcast(podcast_id):
    moderator_id = request.json.get('moderator_id')
    status = request.json.get('status')
    ModerationService().moderate_podcast(podcast_id, moderator_id, status)
    return jsonify({'message': 'Moderation submitted successfully'})
