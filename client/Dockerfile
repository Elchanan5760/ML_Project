FROM python:3.12-slim

# הגדרת ספריית עבודה בתוך הקונטיינר
WORKDIR /app

# העתקת requirements.txt מהספרייה שמעל (../)
COPY requirements.txt ./


# התקנת תלויות
RUN pip install --no-cache-dir -r requirements.txt

# העתקת קוד האפליקציה
COPY . .

# הרצת FastAPI עם uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
