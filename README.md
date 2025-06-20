# 🪞 MoodMirror++

**Real-Time Emotion, Gender, and Cat Detection using AI + Computer Vision**

MoodMirror++ is an intelligent real-time mirror system that detects human faces, analyzes their **gender and emotion**, and also identifies **cats** in the camera feed — whether real or on a screen. Built with modular Python code, this project simulates a smart visual assistant that responds instantly to what it sees.

---

## 🚀 Features

- 👩‍🦰 **Human Face Detection**  
  Detects human faces and classifies their gender and emotional state using DeepFace.

- 🐱 **Cat Detection**  
  Identifies cats using Haar cascades, even from printed or digital images.

- 📦 **Real-Time Processing**  
  Live webcam feed with real-time labeling and bounding boxes.

- 🧩 **Modular Code Structure**  
  Organized like a mid/senior-level project, with scalable file separation for each task.

---

## 🛠️ Tech Stack

- Python 3.x
- OpenCV
- DeepFace
- Haar Cascades (for cat detection)
- Pillow

---

## 📁 Project Structure
MoodMirror/
├── app.py
└── detectors/
├── face_emotion.py # Human face & emotion analysis
└── cat_detector.py # Cat detection


---

## 🧪 Setup & Run

``bash
git clone https://github.com/yourusername/moodmirror.git
cd moodmirror
pip install opencv-python deepface
python app.py

Press Q to quit the webcam feed.

----

Sample Output

The system accurately labels people as:
→ human • woman • happy
→ human • man • neutral
and also labels cats as:
→ cat • detected

![moodmirror_collage](https://github.com/user-attachments/assets/37fcf552-f381-4dcd-b11c-fd7307f7ef17)



---

Roadmap
 Streamlit GUI for image upload & camera toggle

 Cat breed classification (British, Persian, Siamese, etc.)

 Face ID-based personalization

 Emotion trends over time (logging + chart)

 Mobile version (via DroidCam or native app)


 ---

Author
Developed by Ü. Ezgi Akbaş

An aspiring AI/ML engineer blending creativity with machine intelligence.

GitHub → @ulkumezgiakbas
LinkedIn → https://www.linkedin.com/in/uezgiakbas/

---

License
This project is for portfolio purposes. Use it, build on it, just don't forget to credit.

MoodMirror++ is more than a project — it’s an intelligent reflection of how we look at ourselves... and our cats. 🧠🐱

