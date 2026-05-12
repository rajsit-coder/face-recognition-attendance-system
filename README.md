# 📸 Face Recognition Attendance System

A simple AI/ML based Face Recognition Attendance System built using:

* Python
* OpenCV
* Machine Learning (KNN)
* NumPy
* Pickle
* Streamlit

This project captures face data using webcam, trains a KNN model for recognition, and automatically marks attendance into CSV files.

---

# 🚀 Features

✅ Face Registration

✅ Real-Time Face Recognition

✅ Automatic Attendance Marking

✅ Unknown Face Detection

✅ Voice Confirmation

✅ CSV Attendance Storage

✅ Streamlit Dashboard

✅ Beginner Friendly Project

---

# 🧠 Technologies Used

| Technology    | Purpose                            |
| ------------- | ---------------------------------- |
| Python        | Main programming language          |
| OpenCV        | Face detection and webcam handling |
| NumPy         | Array and image processing         |
| Pickle        | Saving face data                   |
| Scikit-learn  | Machine learning model             |
| KNN Algorithm | Face recognition                   |
| CSV           | Attendance storage                 |
| Streamlit     | Attendance dashboard               |
| pywin32       | Voice assistant                    |

---

# 📂 Project Structure

```bash
Face_Recognition_Attendance_System/
│
├── add_faces.py
├── attendance.py
├── app.py
│
├── data/
│   ├── names.pkl
│   ├── faces_data.pkl
│   └── haarcascade_frontalface_default.xml
│
├── Attendance/
│
└── README.md
```

---

# ⚙️ Installation

## Step 1 — Clone Repository

```bash
git clone https://github.com/rajsit-coder/face-recognition-attendance-system.git
```

---

## Step 2 — Open Project Folder

```bash
cd face-recognition-attendance-system
```

---

## Step 3 — Install Required Packages

```bash
pip install opencv-python numpy pandas scikit-learn streamlit pywin32
```

OR

```bash
pip install -r requirements.txt
```

---

# 📥 Download Haar Cascade File

Download:

```text
haarcascade_frontalface_default.xml
```
Official Download Link:

https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml

Place it inside:

```text
data/
```

---

# 📌 How Project Works

The project works in 3 major steps:

```text
1. Register Face
2. Recognize Face
3. Mark Attendance
```

---

# 🧑 Step 1 — Register Face

Run:

```bash
python add_faces.py
```

### Process:

* Webcam opens
* Enter your name
* System captures 100 face images
* Face data gets saved into:

```text
data/faces_data.pkl
data/names.pkl
```

### Important:

* Keep only one face in camera
* Use good lighting
* Move face slightly left/right
* Wait until 100 images collected

---

# 🤖 Step 2 — Take Attendance

Run:

```bash
python attendance.py
```

### Process:

* Webcam opens
* Face gets detected
* KNN predicts person name
* Attendance automatically saved
* Voice confirmation plays
* Camera closes automatically

Attendance CSV stored inside:

```text
Attendance/
```

Example:

```text
Attendance_13-05-2026.csv
```

---

# 🌐 Step 3 — Open Dashboard

Run:

```bash
streamlit run app.py
```

Open browser:

```text
http://localhost:8501
```

### Dashboard Features:

* View attendance
* Download CSV files
* Select attendance date

---

# 🧠 Machine Learning Used

## KNN Algorithm

This project uses:

```text
K-Nearest Neighbors (KNN)
```

### Why KNN?

* Simple
* Beginner friendly
* Fast for small datasets
* Good for real-time prediction

---

# 📌 Face Detection vs Face Recognition

| Face Detection      | Face Recognition  |
| ------------------- | ----------------- |
| Finds face location | Identifies person |
| Uses Haar Cascade   | Uses KNN          |

---

# 📌 How Face Recognition Works

1. Webcam captures image
2. OpenCV detects face
3. Face is resized to 50×50
4. Image converted into feature vector
5. KNN compares with stored faces
6. Nearest match gets predicted
7. Attendance saved in CSV

---

# 📌 Unknown Face Detection

The system checks face distance using:

```python
knn.kneighbors()
```

If distance is too high:

```text
Unknown
```

face is shown.

This prevents random attendance marking.

---

# 📌 Attendance CSV Format

| NAME  | TIME     |
| ----- | -------- |
| Rahul | 10:15:22 |
| Priya | 10:16:01 |

---

# 📌 Important Files

| File           | Purpose                     |
| -------------- | --------------------------- |
| add_faces.py   | Register new face           |
| attendance.py  | Face recognition attendance |
| app.py         | Streamlit dashboard         |
| names.pkl      | Stores labels               |
| faces_data.pkl | Stores face vectors         |

---

# 📌 Advantages

✅ Automatic attendance

✅ Reduces manual work

✅ Real-time recognition

✅ Simple and lightweight

✅ Beginner AI/ML project

---

# 📌 Limitations

❌ Lighting affects accuracy

❌ Small dataset project

❌ Basic machine learning model

❌ Not suitable for very large datasets

---

# 📌 Future Improvements

* Deep Learning (CNN / FaceNet)
* Cloud database integration
* Mobile app support
* Multiple camera support
* Better accuracy
* Anti-spoofing detection

---

# 📌 Viva Questions & Answers

## Q1. What is OpenCV?

OpenCV is an open-source computer vision library used for image and video processing.

---

## Q2. What is Haar Cascade?

Haar Cascade is a pretrained face detection algorithm provided by OpenCV.

---

## Q3. Why use grayscale images?

Grayscale reduces computation and improves detection speed.

---

## Q4. Why resize images?

Machine learning models require fixed-size input.

---

## Q5. Why use KNN?

KNN is simple, fast, and suitable for small datasets.

---

## Q6. What is Pickle?

Pickle stores Python objects into binary files.

---

## Q7. Difference between detection and recognition?

Detection finds face location.
Recognition identifies whose face it is.

---

## Q8. How attendance is stored?

Attendance is stored in CSV files using Python CSV module.

---

# 📌 Commands Summary

## Register Face

```bash
python add_faces.py
```

---

## Take Attendance

```bash
python attendance.py
```

---

## Open Dashboard

```bash
streamlit run app.py
```

---

# 📌 Author

Developed as an AI/ML Internship Project using Python, OpenCV, and Machine Learning.

---

# ⭐ Conclusion

This project demonstrates the practical implementation of:

* Computer Vision
* Face Detection
* Face Recognition
* Machine Learning
* Real-Time Attendance Automation

using Python and OpenCV.
