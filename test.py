import librosa
import librosa.feature 
import librosa.display
import matplotlib.pyplot as plt
from scipy import signal
def convert_audio_to_spectogram(filename,sampleRate):
    # sr == sampling rate 
    x, sr = librosa.load(filename, sr=20000)
    out = signal.hilbert(x)
    # ... and plot, magic!
    plt.figure(figsize=(50, 50))
    librosa.display.specshow(out, sr = sr, x_axis = 'time', y_axis = 'hz')
    plt.savefig("gram.jpg")
convert_audio_to_spectogram("sunset_audio.ogg",None)