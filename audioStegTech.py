import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavfile

'''Takes the Least Signidificant Bits of an audio file and logs them'''


def LittleEndianBits(audio):
    pass


'''Takes the Most Signidificant Bits of an audio file and logs them'''


def BigEndianBits(audio):
    pass


'''creates a spectrogram of an audio file'''


def spectrogram(audio):
    Fs, Audio = wavfile.read(audio)
    Audio = Audio[:, 0]
    first = Audio[:int(Fs*125)]
    powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
    plt.show()


'''converts non wav files to wav'''


def convertToWav(audio):
    pass



'''decodes SSTV signals from an audio file'''


def SSTVdecode(audio, mode):
    pass


spectrogram("test resources/example.wav")
