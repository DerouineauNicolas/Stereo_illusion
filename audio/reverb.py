#!/usr/bin/env python3
#Simple delay line Reverb


import numpy as np
import sounddevice as sd
import wave as wavereader

waveinst = wavereader.open("Guitar-C3.wav")
wavebytes = waveinst.readframes(waveinst.getnframes());

wavetmp = np.frombuffer(wavebytes, dtype="int16")
wave = np.copy(wavetmp)

decay = 0.8
delayMilliseconds = 500
delaySamples = int(delayMilliseconds * 44.1)

print (delaySamples)

for i in range(1,(len(wave)-delaySamples)):
    wave[i + delaySamples] += wave[i] * decay

sd.default.samplerate = waveinst.getframerate()
sd.default.channels = 2

print ("Playing sound with no reverb")

result = np.hstack((wavetmp.reshape(-1, 1), wavetmp.reshape(-1,1)))
sd.play(result, blocking=True)

print ("Playing sound with reverb")

# Convert it to wav format (16 bits)
result = np.hstack((wave.reshape(-1, 1), wave.reshape(-1,1)))
wav_wave = np.array(result, dtype=np.int16)

sd.play(wav_wave, blocking=True)

waveinst.close()
