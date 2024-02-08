import librosa
import librosa.display
import matplotlib.pyplot as plt



'''Takes the Least Signidificant Bits of an audio file and logs them'''


def LittleEndianBits(audio):
    f = open("myfile.jpg", "rb")




'''Takes the Most Signidificant Bits of an audio file and logs them'''


def BigEndianBits(audio):
    pass


'''creates a spectrogram of an audio file'''


def spectrogram(audio,sampleRate):
    x, sr = librosa.load(audio, sr=sampleRate)
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    plt.figure(figsize=(14, 5))
    librosa.display.specshow(Xdb, sr = sr, x_axis = 'time', y_axis = 'hz')
    #change this for server purposes ig once im ready for it
    plt.savefig("gram.jpg")


def convertToWav(audio):
    pass


'''decodes SSTV signals from an audio file'''


def SSTVdecode(audio, mode):
    pass


spectrogram("sunset_audio.ogg",7000)
