from app.models.podcast import Podcast
from app.utils.db_utils import session

class PodcastService:
    @staticmethod
    def get_all_podcasts():
        return session.query(Podcast).all()

    @staticmethod
    def get_podcast_by_id(podcast_id):
        return session.query(Podcast).get(podcast_id)
