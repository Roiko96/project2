# app.py # שם הקובץ
# יישום Flask לניהול ציונים של משחקים
# יישום זה כולל פונקציות להוספת, מחיקת, מיון וחישוב ממוצע ציונים
from flask import Flask, render_template, request, redirect # ייבוא Flask, render_template, request ו-redirect
from functions import scores, add_score_data, delete_score_by_name, sort_scores_by_key, calculate_average # ייבוא הפונקציות מהמודול functions

app = Flask(__name__)# יצירת מופע של Flask

@app.route("/")# הגדרת הנתיב הבסיסי של היישום
def index():#   פונקציה להצגת הדף הראשי
    # קריאה לפונקציה לקבלת הציונים
    return render_template("index.html", scores=scores)# החזרת התבנית index.html עם הציונים

@app.route("/add", methods=["POST"])# הגדרת נתיב להוספת ציונים
def add():# פונקציה להוספת ציונים
    name = request.form["name"]# קבלת שם השחקן מהטופס
    game = request.form["game"]# קבלת שם המשחק מהטופס
    try:# ניסיון להמיר את הציון למספר עשרוני
        score = float(request.form["score"])# קבלת הציון מהטופס
        add_score_data(name, game, score)# הוספת הציון למאגר הנתונים
    except ValueError:# אם יש שגיאה בהמרת הציון למספר עשרוני
        pass# התעלמות מהשגיאה
    return redirect("/")# הפניה חזרה לדף הראשי

@app.route("/delete", methods=["POST"])# הגדרת נתיב למחיקת ציונים
def delete():# פונקציה למחיקת ציונים
    name = request.form["name"] # קבלת שם השחקן מהטופס
    delete_score_by_name(name) # מחיקת הציון של השחקן מהמאגר
    return redirect("/") # הפניה חזרה לדף הראשי

@app.route("/sort/<key>") # הגדרת נתיב למיון ציונים לפי מפתח
def sort(key): # פונקציה למיון ציונים
    sort_scores_by_key(key)
    return redirect("/")

@app.route("/average")
def average():
    avg = calculate_average()
    return render_template("index.html", scores=scores, average=avg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
# הקוד מוגש כקובץ app.py
# כדי להריץ את היישום, יש לוודא שהתקנת את Flask
# ולהתקין את התלויות הדרושות עם pip:
# pip install Flask
# לאחר מכן, יש לשמור את הקוד בקובץ app.py
# ולאחר מכן ניתן להריץ את היישום על ידי הפעלת הקובץ
# app.py
# קוד זה הוא יישום Flask פשוט לניהול ציונים של משחקים
# יש לוודא שהקובץ functions.py קיים באותה התיקייה עם הפונקציות המתאימות
# יש לוודא שהקובץ index.html קיים בתיקיית templates עם התבנית המתאימה
# יש לוודא שהקובץ functions.py קיים באותה התיקייה עם הפונקציות המתאימות
# ולהריץ את הקובץ עם הפקודה: python app.py