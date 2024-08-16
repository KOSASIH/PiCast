# app/content_based_filtering.py
from sklearn.neighbors import NearestNeighbors
from app.audio_features import extract_audio_features

class ContentBasedFiltering:
    def __init__(self, podcast_episodes):
        self.podcast_episodes = podcast_episodes
        self.audio_features = self.extract_audio_features()
        self.model = self.build_model()

    def extract_audio_features(self):
        audio_features = []
        for episode in self.podcast_episodes:
            audio_features.append(extract_audio_features(episode['audio_file']))
        return np.array(audio_features)

    def build_model(self):
        model = NearestNeighbors(n_neighbors=5, algorithm='ball_tree')
        model.fit(self.audio_features)
        return model

    def predict_recommendations(self, podcast_id):
        podcast_vector = self.audio_features[podcast_id]
        distances, indices = self.model.kneighbors([podcast_vector])
        return indices[0]
