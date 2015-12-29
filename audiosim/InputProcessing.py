import numpy as np
import librosa
y, sr = librosa.core.load("Warduji-Prog.wav", duration=20)
print y
print sr

# Tim Huynh was here