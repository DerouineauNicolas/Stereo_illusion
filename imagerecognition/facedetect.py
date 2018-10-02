import numpy as np
from matplotlib import pyplot as plt
import sounddevice as sd

sd.default.samplerate = 44100
sd.default.channels = 2
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

time = 1.0
# Generate time of samples between 0 and two seconds
samples = np.arange(44100 * time) / 44100.0
# Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
frequency1 = 440
wave = 10000 * np.sin(2 * np.pi * frequency1 * samples)

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,    scaleFactor=1.2, minNeighbors=5)

    for (x,y,w,h) in faces:
        img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        frequency1=(y*10)
        wave = 10000 * np.sin(2 * np.pi * frequency1 * samples)
        result = np.hstack((wave.reshape(-1, 1), wave.reshape(-1, 1)))
        # Convert it to wav format (16 bits)
        wav_wave = np.array(result, dtype=np.int16)
        sd.play(wav_wave, blocking=False)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()