from flask import Flask, jsonify, request
from app.highscores import get_all_scores, get_score_by_id, save_score
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    return "<h1>API -> </h1>"


@app.route('/api/v1/scores', methods=['GET'])
def scores():
    return jsonify(get_all_scores())


@app.route('/api/v1/scores/<string:listname>', methods=['GET'])
def score_list(listname):
    return jsonify(get_all_scores())


@app.route('/api/v1/scores', methods=['PUT', 'POST'])
def new_score():
    new = save_score(request.get_json())
    return jsonify(new)


@app.route('/api/v1/scores/<int:id>')
def score(id):
    one = get_score_by_id(id)
    if one is None:
        return jsonify({"error": 404, "message": "Not found"}), 404
    return jsonify(one)


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": 404, "message": "Not found"}), 404
