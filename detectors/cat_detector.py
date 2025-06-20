import cv2

cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

def detect_cat(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cats = cat_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return cats
