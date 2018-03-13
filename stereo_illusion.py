#!/usr/bin/env python3
#This programm demonstrates the stereo illusion
#coming from playing sinewave with close frequencies in stereo (ie: one sine per ears).
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

#The following conclusion can be done:
#When frequency difference is between 1 to 15Hz, a Beat effect is perceived.
#When it's higher, polyphony is perceived.
#This phenomena prooves that the brain is adding the two sounds.
#Beat can be explained by the fact that:
#cos(2piF0t)+cos(2pi(F0+df)t)=2cos(2pi(F0+df)t)cos(2*pi*(df/2)t)
