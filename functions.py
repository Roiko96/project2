# functions.py
scores = []  # רשימת ניקוד גלובלית

def add_score_data(name, game, score):
    scores.append({"name": name, "game": game, "score": score})

def delete_score_by_name(name):
    global scores
    scores = [s for s in scores if s["name"] != name]

def sort_scores_by_key(key):
    reverse = key == "score"
    scores.sort(key=lambda x: x[key], reverse=reverse)

def calculate_average():
    if not scores:
        return 0
    return sum(s["score"] for s in scores) / len(scores)

def edit_score_data(current_name, current_game, new_name, new_game, new_score):
    for s in scores:
        if s["name"] == current_name and s["game"] == current_game:
            s["name"] = new_name
            s["game"] = new_game
            s["score"] = new_score
            break
