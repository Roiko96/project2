FROM python:3.12-slim  # מבוסס על Python מינימלי
WORKDIR /app           # הגדרת תיקיית עבודה
COPY . .               # העתקת כל קבצי הפרויקט
RUN pip install -r requirements.txt  # התקנת התלויות
EXPOSE 5000            # פתיחת פורט 5000
CMD ["python", "app.py"]  # הרצת הקובץ הראשי
