scores = [] # רשימה לאחסון ניקודים

def add_score(): # פונקציה להוספת ניקוד
    name = input("Enter player name: ") # מבקש מהמשתמש להזין שם שחקן
    game = input("Enter game name: ") # מבקש מהמשתמש להזין שם משחק
    while True: # לולאת while לבדיקת תקינות הניקוד
        try: # מבקש מהמשתמש להזין ניקוד
            score = float(input("Enter score: ")) # מנסה להמיר את הקלט למספר עשרוני
            break # אם ההמרה הצליחה, יוצא מהלולאה
        except ValueError: # אם ההמרה נכשלה
            print("Invalid score. Please enter a number.") # מציג הודעת שגיאה ומבקש להזין ניקוד מחדש
    scores.append({"name": name, "game": game, "score": score}) # מוסיף את הניקוד לרשימת הניקודים
    print("Score added successfully.") # מציג הודעת הצלחה על הוספת הניקוד

def show_scores(): # פונקציה להצגת ניקודים
    if not scores: # אם הרשימה ריקה
        print("No scores to show.") # מציג הודעה שאין ניקודים להציג
        return # יוצא מהפונקציה
    for player in scores: # עובר על כל השחקנים ברשימת הניקודים
        print(f"Name: {player['name']}, Game: {player['game']}, Score: {player['score']}") # מציג את שם השחקן, שם המשחק והניקוד שלו

def delete_score(): # פונקציה למחיקת ניקוד
    name = input("Enter player name to delete: ") # מבקש מהמשתמש להזין שם שחקן למחיקה
    for player in scores: # עובר על כל השחקנים ברשימת הניקודים
        if player["name"] == name: # אם שם השחקן תואם לשם שהוזן
            scores.remove(player) # מסיר את השחקן מהרשימה
            print(f"{name} removed successfully.") # מציג הודעת הצלחה על מחיקת השחקן
            return # יוצא מהפונקציה
    print(f"{name} not found.") # אם השחקן לא נמצא, מציג הודעת שגיאה

def sort_scores(): # פונקציה למיון ניקודים
    print("Sort by:") # מציג אפשרויות מיון
    print("1. Name") # אפשרות למיון לפי שם
    print("2. Game") # אפשרות למיון לפי משחק
    print("3. Score") # אפשרות למיון לפי ניקוד
    
    choice = input("Enter your choice: ") # מבקש מהמשתמש להזין אפשרות מיון

    if choice == "1": # אם המשתמש בחר למיין לפי שם
        sorted_list = sorted(scores, key=lambda x: x["name"]) # ממיין את הרשימה לפי שם השחקן
        print("Sorted names:") # מציג את השמות הממוינים
        for p in sorted_list: # עובר על הרשימה הממוינת
            print(p["name"]) # מציג את שם השחקן

    elif choice == "2": # אם המשתמש בחר למיין לפי משחק
        sorted_list = sorted(scores, key=lambda x: x["game"]) # ממיין את הרשימה לפי שם המשחק
        print("Sorted games:") # מציג את המשחקים הממוינים
        for p in sorted_list: # עובר על הרשימה הממוינת
            print(p["game"]) # מציג את שם המשחק

    elif choice == "3": # אם המשתמש בחר למיין לפי ניקוד
        sorted_list = sorted(scores, key=lambda x: x["score"], reverse=True) # ממיין את הרשימה לפי ניקוד בסדר יורד
        print("Sorted scores (highest to lowest):") # מציג את הניקודים הממוינים מהגבוה לנמוך
        for p in sorted_list: # עובר על הרשימה הממוינת
            print(p["score"]) # מציג את הניקוד

    else: # אם המשתמש הזין אפשרות לא תקינה
        print("Invalid sort option.") # מציג הודעת שגיאה על אפשרות מיון לא תקינה



def average_score(): # פונקציה לחישוב ממוצע ניקוד
    if not scores: # אם הרשימה ריקה
        print("No scores available.") # מציג הודעה שאין ניקודים זמינים
        return # יוצא מהפונקציה
    avg = sum(p["score"] for p in scores) / len(scores) # מחשב את ממוצע הניקודים
    print(f"Average score: {avg:.2f}") # מציג את ממוצע הניקודים בפורמט עם שתי ספרות אחרי הנקודה

def edit_score(): # פונקציה לעריכת ניקוד
    name = input("Enter player name to edit: ") # מבקש מהמשתמש להזין שם שחקן לעריכה
    game = input("Enter game name to edit: ") # מבקש מהמשתמש להזין שם משחק לעריכה
    found = False # משתנה לבדיקת האם נמצא שחקן לעריכה

    for player in scores: # עובר על כל השחקנים ברשימת הניקודים
        if player["name"] == name and player["game"] == game: # אם שם השחקן ושם המשחק תואמים לשמות שהוזנו
            print("What would you like to edit?") # מציג אפשרויות עריכה
            print("1. Name") # אפשרות לעריכת שם השחקן
            print("2. Game") # אפשרות לערwsl שם המשחק
            print("3. Score") # אפשרות לעריכת הניקוד
            print("4. All of them") # אפשרות לעריכת כל השדות
            choice = input("Enter your choice: ") # מבקש מהמשתמש להזין אפשרות עריכה
            if choice == "1": # אם המשתמש בחר לערוך את שם השחקן
                new_name = input("Enter new name: ") # מבקש מהמשתמש להזין שם חדש לשחקן
                player["name"] = new_name # מעדכן את שם השחקן ברשימה
                print("Name updated.") # מציג הודעת הצלחה על עדכון השם
            elif choice == "2": # אם המשתמש בחר לערוך את שם המשחק
                new_game = input("Enter new game name: ") # מבקש מהמשתמש להזין שם חדש למשחק
                player["game"] = new_game # מעדכן את שם המשחק ברשימה
                print("Game updated.") # מציג הודעת הצלחה על עדכון שם המשחק
            elif choice == "3": # אם המשתמש בחר לערוך את הניקוד
                while True: # לולאת while לבדיקת תקינות הניקוד
                    try: # מבקש מהמשתמש להזין ניקוד חדש
                        new_score = float(input("Enter new score: ")) # מנסה להמיר את הקלט למספר עשרוני
                        player["score"] = new_score # מעדכן את הניקוד ברשימה
                        print("Score updated.") # מציג הודעת הצלחה על עדכון הניקוד
                        break # אם ההמרה הצליחה, יוצא מהלולאה
                    except ValueError: # אם ההמרה נכשלה
                        print("Invalid score. Please enter a number.") # מציג הודעת שגיאה ומבקש להזין ניקוד מחדש
            elif choice == "4": # אם המשתמש בחר לערוך את כל השדות
                new_name = input("Enter new name: ") # מבקש מהמשתמש להזין שם חדש לשחקן
                new_game = input("Enter new game name: ") # מבקש מהמשתמש להזין שם חדש למשחק
                while True: # לולאת while לבדיקת תקינות הניקוד
                    try: # מבקש מהמשתמש להזין ניקוד חדש
                        new_score = float(input("Enter new score: ")) # מנסה להמיר את הקלט למספר עשרוני
                        break # אם ההמרה הצליחה, יוצא מהלולאה
                    except ValueError: # אם ההמרה נכשלה
                        print("Invalid score. Please enter a number.") # מציג הודעת שגיאה ומבקש להזין ניקוד מחדש
                player["name"] = new_name # מעדכן את שם השחקן ברשימה
                player["game"] = new_game # מעדכן את שם המשחק ברשימה
                player["score"] = new_score # מעדכן את הניקוד ברשימה
                print("All fields updated.") # מציג הודעת הצלחה על עדכון כל השדות
            else: # אם המשתמש הזין אפשרות לא תקינה
                print("Invalid choice.") # מציג הודעת שגיאה על אפשרות עריכה לא תקינה

            found = True # מעדכן את המשתנה found אם נמצא שחקן לעריכה
            break # יוצא מהלולאה אם נמצא שחקן לעריכה

    if not found: # אם לא נמצא שחקן לעריכה
        print(f"No entry found for player {name} and game {game}.") # מציג הודעת שגיאה על כך שלא נמצא שחקן עם השם והמשחק שהוזנו


