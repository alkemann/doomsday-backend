
aid = 3
scores = [
    {
        "id": 1,
        "list": "2022:8",
        "name": "Alexander",
        "score": 15,
        "time": 12
    },
    {
        "id": 2,
        "list": "2022:8",
        "name": "Alexander",
        "score": 14,
        "time": 16
    },
]


def get_all_scores():
    global scores
    return scores


def get_score_by_id(id):
    global scores
    for s in scores:
        if s['id'] == id:
            return s
    return None


def save_score(data):
    global aid, scores
    data["id"] = aid
    aid = aid + 1
    scores.append(data)
    return data
