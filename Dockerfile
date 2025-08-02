FROM python:3.12-slim 
# מתוך פייתון 3.12 גרסה דקה
WORKDIR /app 
# הגדרת ספריית העבודה בתוך הקונטיינר
COPY main.py functions.py ./
# העתקת הקבצים main.py ו-functions.py לתוך ספריית העבודה
CMD ["python", "main.py"]
# הפקודה שתופעל כאשר הקונטיינר יתחיל
