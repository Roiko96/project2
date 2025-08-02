scores = []

def add_score_data(name, game, score):
    scores.append({"name": name, "game": game, "score": float(score)})

def delete_score_by_name(name):
    global scores
    scores = [s for s in scores if s["name"] != name]

def sort_scores_by_key(key):
    if key in ["name", "game", "score"]:
        scores.sort(key=lambda x: x[key], reverse=(key == "score"))

def calculate_average():
    if not scores:
        return 0
    return sum(s["score"] for s in scores) / len(scores)
