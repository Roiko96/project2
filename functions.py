# רשימה שמכילה את כל הציונים שהוזנו
scores = []

# פונקציה להוספת ציון חדש לרשימה
def add_score_data(name, game, score):
    scores.append({"name": name, "game": game, "score": score})

# פונקציה למחיקת ציון לפי שם שחקן
def delete_score_by_name(name):
    global scores
    scores = [s for s in scores if s["name"] != name]

# פונקציה למיון הרשימה לפי מפתח (name / game / score)
def sort_scores_by_key(key):
    reverse = key == "score"  # ניקוד נרצה למיין מהגבוה לנמוך
    scores.sort(key=lambda x: x[key], reverse=reverse)

# פונקציה שמחזירה את ממוצע הציונים
def calculate_average():
    if not scores:
        return 0
    return sum(s["score"] for s in scores) / len(scores)

# פונקציה לעריכת ציון קיים לפי שם ומשחק
def edit_score_data(current_name, current_game, new_name, new_game, new_score):
    for s in scores:
        if s["name"] == current_name and s["game"] == current_game:
            s["name"] = new_name
            s["game"] = new_game
            s["score"] = new_score
            break
