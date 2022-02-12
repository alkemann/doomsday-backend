from flask import Flask, jsonify, request
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
env_config = os.getenv("FLASK_ENV", "config.DevelopmentConfig")
app.config.from_object(env_config)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Score


@app.route('/', methods=['GET'])
def route_home():
    return f"<h1>API that'a way {app.config.get('SECRET')}</h1>"


@app.route('/api/v1/scores', methods=['GET'])
def route_scores_index():
    return jsonify([])


# @app.route('/api/v1/scores/<string:listname>', methods=['GET'])
# def route_score_single_list(listname):
#     return jsonify(get_all_scores())


@app.route('/api/v1/scores', methods=['PUT', 'POST'])
def route_add_score():
    post = request.get_json()
    try:
        score = Score(
            points=post["score"],
            time=post["time"],
            name=post["name"]
        )
        db.session.add(score)
        db.session.commit()
        return jsonify(score.json())
    except Exception:
        return jsonify({"error": 500, "message": "Failed to save"}), 500


@app.route('/api/v1/scores/<int:id>')
def route_get_score_by_id(id):
    one = get_score_by_id(id)
    if one is None:
        return jsonify({"error": 404, "message": "Not found"}), 404
    return jsonify(one)


@app.errorhandler(404)
def route_page_not_found(e):
    return jsonify({"error": 404, "message": "Not found"}), 404
