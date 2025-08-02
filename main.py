from functions import * # מייבא את כל הפונקציות מהקובץ functions.py

def main(): # פונקציית main שמכילה את התפריט הראשי
    while True: # לולאת while שממשיכה לרוץ עד שהמשתמש בוחר לצאת
        print("\nmenu:") # מציגה את התפריט הראשי
        print("1. add score") # הוספת ניקוד
        print("2. show scores") # הצגת ניקודים
        print("3. delete score") # מחיקת ניקוד
        print("4. sort scores") # מיון ניקודים
        print("5. average score") # חישוב ממוצע ניקוד
        print("6. edit score") # עריכת ניקוד
        print("7. exit") # יציאה מהתוכנית

        choice = input("choose an option: ") # מבקש מהמשתמש לבחור אפשרות מהתפריט

        if choice == "1": # אם המשתמש בחר להוסיף ניקוד
            add_score() # פונקציה להוספת ניקוד
        elif choice == "2": # אם המשתמש בחר להציג ניקודים
            show_scores() # פונקציה להצגת ניקודים
        elif choice == "3": # אם המשתמש בחר למחוק ניקוד
            delete_score() # פונקציה למחיקת ניקוד
        elif choice == "4": # אם המשתמש בחר למיין ניקודים
            sort_scores() # פונקציה למיון ניקודים
        elif choice == "5": # אם המשתמש בחר לחשב ממוצע ניקוד
            average_score() # פונקציה לחישוב ממוצע ניקוד
        elif choice == "6": # אם המשתמש בחר לערוך ניקוד
            edit_score() # פונקציה לעריכת ניקוד
        elif choice == "7": # אם המשתמש בחר לצאת
            print("Goodbye!") # מציג הודעת פרידה
            break # ויוצא מהלולאה
        else: # אם המשתמש בחר אפשרות לא תקינה
            print("Invalid choice.") # מציג הודעת שגיאה

if __name__ == "__main__": # אם הקובץ רץ כקובץ ראשי
    main() # קורא לפונקציית main
