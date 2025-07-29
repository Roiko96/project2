scores = []

def add_score_data(name, game, score):
    scores.append({"name": name, "game": game, "score": score})

def delete_score_by_name(name):
    global scores
    scores = [s for s in scores if s["name"] != name]

def sort_scores_by_key(key):
    scores.sort(key=lambda s: s.get(key, ""))

def calculate_average():
    if not scores:
        return 0
    return round(sum(s["score"] for s in scores) / len(scores), 2)
