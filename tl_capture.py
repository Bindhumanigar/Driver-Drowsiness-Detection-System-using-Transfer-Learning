import cv2
import numpy as np
from tensorflow.keras.models import load_model
from pygame import mixer

# Load the pre-trained face and eye cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Load the pre-trained model for eye state prediction
model = load_model('models/model.h5')

# Initialize Pygame mixer for sound
mixer.init()
sound = mixer.Sound('alarm.wav')

# Initialize video capture from the default camera (0)
cap = cv2.VideoCapture(0)

# Initialize score variable
score = 0

while True:
    ret, frame = cap.read()
    height, width = frame.shape[0:2]

    # Convert the frame to grayscale for face and eye detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)

    # Iterate over detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        # Region of interest (ROI) for eyes within the detected face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=1)

        # Iterate over detected eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 3)

            # Preprocess the eye image for model prediction
            eye = cv2.resize(roi_color[ey:ey + eh, ex:ex + ew], (80, 80))
            eye = eye / 255.0
            eye = np.expand_dims(eye, axis=0)

            # Model prediction for eye state
            prediction = model.predict(eye)

            # Update score and trigger alarm if eyes are closed
            if prediction[0][0] > 0.30:
                cv2.putText(frame, 'Closed', (10, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                score += 1
                if score > 15:
                    try:
                        sound.play()
                    except:
                        pass
            # Decrement score if eyes are open
            elif prediction[0][1] > 0.90:
                cv2.putText(frame, 'Open', (10, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 1,
                            cv2.LINE_AA)
                score -= 1
                if score < 0:
                    score = 0

        # Display the current score
        cv2.putText(frame, 'Score: ' + str(score), (100, height - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                    (255, 255, 255), 1, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break

# Release video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
