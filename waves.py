import numpy as np
import keyboard
import sounddevice as sd
from scipy import signal
import matplotlib.pyplot as plt

notes = {
    "A4": 440,
    "B4": 494,
    "C4": 523,
    "D4": 587,
    "E4": 660,
    "F4": 698,
    "G4": 784,
    "A5": 880
}


class Waves:

    def __init__(self):
        return None

    def sine(self, note, amplitude):
        self.amp = amplitude
        self.freq = note  # Hz
        samplingFreq = 44100  # Hz
        nData = 10 * samplingFreq
        time = np.arange(0, nData).T / samplingFreq  # s
        initPhase = np.pi / 2  # rad
        sine = self.amp * np.cos(2 * np.pi * self.freq * time + initPhase)
        return sine

    def square(self, note, amplitude):
        self.amp = amplitude
        self.freq = note  # Hz
        samplingFreq = 44100  # Hz
        nData = 10 * samplingFreq
        time = np.arange(0, nData).T / samplingFreq  # s
        initPhase = np.pi / 2  # rad

        # Using the signal toolbox from scipy for the sawtooth:
        square = self.amp * signal.square(2 * np.pi * self.freq * time + initPhase, duty=0.5)
        # Scale the waveform to a certain amplitude and apply an offset:
        return square

    def saw(self, note, amplitude):
        self.amp = amplitude
        self.freq = note  # Hz
        samplingFreq = 44100  # Hz
        nData = 10 * samplingFreq
        time = np.arange(0, nData).T / samplingFreq  # s
        initPhase = np.pi / 2  # rad

        # Using the signal toolbox from scipy for the sawtooth:
        saw = self.amp * signal.sawtooth(2 * np.pi * self.freq * time + initPhase)
        # Scale the waveform to a certain amplitude and apply an offset:
        return saw


x = Waves()

while True:  # making a loop

    if keyboard.is_pressed('q'):  # if key 'q' is pressed
        sd.stop()
        freq = notes["A4"]
        sinusoid = x.sine(notes["A4"], 1)
        sd.play(sinusoid)

    if keyboard.is_pressed('w'):
        sd.stop()
        freq = notes["A4"]
        square = x.square(notes["A4"], 1)
        sd.play(square)
        t = np.linspace(0, 1, 500)

    if keyboard.is_pressed('e'):
        sd.stop()
        freq = notes["A4"]
        saw = x.saw(notes["A4"], 1)
        sd.play(saw)


