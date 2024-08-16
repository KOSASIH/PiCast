# moderation/moderation_service.py
from flask import current_app
from moderation.moderation_model import Report, Moderation

class ModerationService:
    def report_podcast(self, podcast_id, user_id, reason, description):
        report = Report(podcast_id=podcast_id, user_id=user_id, reason=reason, description=description)
        db.session.add(report)
        db.session.commit()

    def get_reports(self):
        return Report.query.all()

    def moderate_podcast(self, podcast_id, moderator_id, status):
        moderation = Moderation(podcast_id=podcast_id, moderator_id=moderator_id, status=status)
        db.session.add(moderation)
        db.session.commit()

    def get_moderations(self):
        return Moderation.query.all()
