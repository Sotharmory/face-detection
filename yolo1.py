import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Buka kamera (gunakan 0 untuk webcam default)
cap = cv2.VideoCapture(0)

while True:
    # Membaca frame dari kamera
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Balik frame secara horizontal (mirror effect)
    frame = cv2.flip(frame, 1)
    
    # Konversi ke skala abu-abu (deteksi wajah bekerja lebih baik pada grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Deteksi wajah
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Gambar persegi panjang di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Tampilkan hasil frame
    cv2.imshow('Face Detection', frame)
    
    # Tekan 'q' untuk keluar dari loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
