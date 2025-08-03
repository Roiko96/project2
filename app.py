from flask import Flask, render_template, request, redirect
from functions import scores, add_score_data, delete_score_by_name, sort_scores_by_key, calculate_average, edit_score_data

app = Flask(__name__)  # יצירת מופע Flask

@app.route("/")  # דף הבית שמציג את הטבלה
def index():
    return render_template("index.html", scores=scores)

@app.route("/add", methods=["POST"])  # הוספת ציון חדש
def add():
    name = request.form["name"]
    game = request.form["game"]
    try:
        score = float(request.form["score"])
        add_score_data(name, game, score)
    except ValueError:
        pass  # אם הקלט לא תקין מתעלמים
    return redirect("/")

@app.route("/delete", methods=["POST"])  # מחיקת שחקן לפי שם
def delete():
    name = request.form["name"]
    delete_score_by_name(name)
    return redirect("/")

@app.route("/sort/<key>")  # מיון לפי שדה (name/game/score)
def sort(key):
    sort_scores_by_key(key)
    return redirect("/")

@app.route("/average")  # הצגת ממוצע
def average():
    avg = calculate_average()
    return render_template("index.html", scores=scores, average=avg)

@app.route("/edit", methods=["POST"])  # עריכת ציון
def edit():
    current_name = request.form["current_name"]
    current_game = request.form["current_game"]
    new_name = request.form["new_name"]
    new_game = request.form["new_game"]
    try:
        new_score = float(request.form["new_score"])
        edit_score_data(current_name, current_game, new_name, new_game, new_score)
    except ValueError:
        pass
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # הפעלת השרת בפורט 5000
