from flask import Flask
from app.routes.podcast_routes import podcast_blueprint
from app.routes.user_routes import user_blueprint

app = Flask(__name__)
app.register_blueprint(podcast_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
