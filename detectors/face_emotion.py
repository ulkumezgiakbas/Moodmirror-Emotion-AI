from deepface import DeepFace

def analyze_face(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion', 'gender'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
        gender = result[0]['dominant_gender']
        return f"{gender} * {emotion}"
    except Exception as e:
        return None
