Face Detection with OpenCV
📌 Project Overview
This project demonstrates a simple yet powerful real-time face detection system using OpenCV in Python. The system leverages the classic Haar Cascade Classifier, a machine learning-based approach where a cascade function is trained with a lot of positive and negative images to detect objects—in this case, human faces.

The application captures live video feed from the webcam, processes each frame to detect faces, and draws bounding boxes around them. To make the interaction more natural and intuitive, the video stream is horizontally flipped to mimic a mirror view—similar to how you would see yourself on a front-facing camera.

✨ Features
🎥 Real-time Face Detection: Continuously detects and tracks human faces through the webcam stream with minimal latency.

🪞 Mirror Effect: Applies a horizontal flip to the video feed, creating a mirror-like experience for the user.

📦 Pre-trained Classifier: Utilizes OpenCV’s pre-trained Haar Cascade Classifier for accurate and lightweight face detection.

📸 Visual Feedback: Displays real-time bounding boxes over detected faces in the video window.

⚙️ Lightweight and Efficient: Requires minimal hardware and computational resources, making it suitable for most machines.
