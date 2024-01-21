# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

'''Takes the Least Signidificant Bits of an audio file and logs them'''


def LittleEndianBits(audio):
    pass


'''Takes the Most Signidificant Bits of an audio file and logs them'''


def BigEndianBits(audio):
    pass


'''creates a spectrogram of an audio file'''


def spectrogram(audio):
    Fs, aud = wavfile.read('test resources/example.wav')
    # select left channel only
    aud = aud[:,0]
    # trim the first 125 seconds
    first = aud[:int(Fs*125)]
    powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first, Fs=Fs)
    plt.show()


'''converts non wav files to wav'''


def convertToWav(audio):
    pass


'''decodes SSTV signals from an audio file'''


def SSTVdecode(audio, mode):
    pass


spectrogram("test resources/example.wav")
