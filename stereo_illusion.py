#!/usr/bin/env python3
#This programm demonstrates the stereo illusion
#coming from playing sinewave with close frequency in different ears
#To install dependencies
#pip3 install numpy sounddevice
 

import numpy as np
import sounddevice as sd

sd.default.samplerate = 44100
sd.default.channels = 2

time = 10.0
frequency1 = 440
frequency2 = 460

# Generate time of samples between 0 and two seconds
samples = np.arange(44100 * time) / 44100.0
# Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
wave = 10000 * np.sin(2 * np.pi * frequency1 * samples)
wave2 = 10000 * np.sin(2 * np.pi * frequency2 * samples)
result = np.hstack((wave.reshape(-1, 1), wave2.reshape(-1,1)))

# Convert it to wav format (16 bits)
wav_wave = np.array(result, dtype=np.int16)

sd.play(wav_wave, blocking=True)
