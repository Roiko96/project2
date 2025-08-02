# functions.py - קובץ עם כל הפונקציות הלוגיות של המשחק

scores = []  # רשימה גלובלית לשמירת ניקודים

def add_score_data(name, game, score):
    scores.append({"name": name, "game": game, "score": score})  # מוסיף רשומה חדשה

def delete_score_by_name(name):
    global scores
    scores = [s for s in scores if s["name"] != name]  # מוחק לפי שם

def sort_scores_by_key(key):
    if key in ["name", "game", "score"]:  # מוודא שהמפתח חוקי
        scores.sort(key=lambda x: x[key], reverse=(key == "score"))  # ממיין לפי מפתח

def calculate_average():
    if not scores:
        return 0
    return round(sum(p["score"] for p in scores) / len(scores), 2)  # מחזיר ממוצע

def edit_score_by_name_and_game(name, game, new_name=None, new_game=None, new_score=None):
    for player in scores:
        if player["name"] == name and player["game"] == game:
            if new_name:
                player["name"] = new_name
            if new_game:
                player["game"] = new_game
            if new_score is not None:
                player["score"] = new_score
            return True
    return False
