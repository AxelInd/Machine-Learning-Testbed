# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:42:55 2021

@author: axelt

Based on https://www.youtube.com/watch?v=Oa_d-zaUti8
"""

#best library for audio processing
import librosa, librosa.display

import matplotlib.pyplot as plt
import numpy as np

file = "blues.00000.wav"

#load the file into librosa.
#the sample rate determines the size and training time of the model
#signal: numpy array of samples #samples = signal rate * song length
#sr is just the sample rate we gave as input
signal, sr = librosa.load(file, sr=22500)

#many many samples
print ("shape of signal", signal.shape)

#librosa function to plot wave functions
"""
librosa.display.waveplot(signal,sr=sr)

plt.xlabel("Time")
plt.ylabel("Amplitude")
"""

#FFT to move from time domain to frequency domain
# returns as many values as the number of samples in the wave form
# values are complex numbers
fft=np.fft.fft(signal)

# magnitudes tell us the contribution of each frequency bin to the overall sound
#"The absolute value of a complex number , a+bi (also called the modulus ) 
#is defined as the distance between the origin (0,0) and the point (a,b) in 
#the complex plane."
magnitude=np.abs(fft)
frequency = np.linspace(0,sr,len(magnitude))

"""
plt.plot(frequency,magnitude)
plt.xlabel("Freiquency")
plt.ylabel("Magnitude")
"""

#as an artifact of FFT we get a symmetrical graph, we don't need both halves
#so we only look at the left side
left_frequency =frequency[:int(len(frequency)/2)]
left_magnitude = magnitude[:int(len(magnitude)/2)]

#now the graph is single-tailed
"""
plt.plot(left_frequency,left_magnitude)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
"""

# STFT: short term fourier transform
#size of the window we consider (in our samples)
n_fft = 2048
#how much we move each time (through our samples)
hop_length=512

stft=librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)
#stft contains complex numbers
spectrogram = np.abs(stft)

#good for visualising spectrum-like data
librosa.display.specshow(spectrogram, sr=sr, hop_length = hop_length)
"""
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
"""
#there are bursts of energy at lower frequencies,  but mostly empty

#convert to decibels, makes it much more readable
log_spectrogram = librosa.amplitude_to_db(spectrogram)
"""
librosa.display.specshow(log_spectrogram, sr=sr, hop_length = hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()
"""
#MFCCs: Mel Frequency Capstral Coefficients
#n_mfcc how many coefficents we want
# MFCCs start with an fft
MFFCs = librosa.feature.mfcc(signal, n_fft=n_fft,sr=sr, hop_length=hop_length, n_mfcc=13)

librosa.display.specshow(MFFCs, sr=sr, hop_length = hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar()










#ideas what happens if we just fft and run it through a regular neural network?





















