# app.py - קובץ ראשי להפעלת Flask

from flask import Flask, render_template, request, redirect
from functions import (
    scores,
    add_score_data,
    delete_score_by_name,
    sort_scores_by_key,
    calculate_average,
    edit_score_by_name_and_game
)

app = Flask(__name__)  # יצירת מופע של אפליקציית Flask

@app.route("/")  # דף הבית
def index():
    return render_template("index.html", scores=scores)  # מציג את רשימת הניקודים

@app.route("/add", methods=["POST"])  # נתיב להוספת ניקוד
def add():
    name = request.form["name"]  # מקבל שם מהטופס
    game = request.form["game"]  # מקבל משחק מהטופס
    try:
        score = float(request.form["score"])  # מוודא שהציון מספרי
        add_score_data(name, game, score)  # מוסיף לרשימה
    except ValueError:
        pass  # אם לא מספר – מתעלם
    return redirect("/")  # חוזר לדף הבית

@app.route("/delete", methods=["POST"])  # נתיב למחיקת שחקן
def delete():
    name = request.form["name"]
    delete_score_by_name(name)
    return redirect("/")

@app.route("/sort/<key>")  # נתיב למיון לפי שם/משחק/ניקוד
def sort(key):
    sort_scores_by_key(key)
    return redirect("/")

@app.route("/average")  # נתיב להצגת ממוצע ניקוד
def average():
    avg = calculate_average()
    return render_template("index.html", scores=scores, average=avg)

@app.route("/edit", methods=["POST"])  # נתיב לעריכת שחקן
def edit():
    name = request.form["name"]
    game = request.form["game"]
    new_name = request.form.get("new_name")
    new_game = request.form.get("new_game")
    new_score = request.form.get("new_score")

    try:
        new_score = float(new_score) if new_score else None
    except ValueError:
        new_score = None

    edit_score_by_name_and_game(name, game, new_name, new_game, new_score)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # מפעיל את Flask בכתובת חיצונית
