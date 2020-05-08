import numpy as np
from scipy import signal

notes = {  # maps keyboard keys to musical notes
    "a": 440,  # A4
    "s": 494,  # B4
    "d": 523,  # C4
    "f": 587,  # D4
    "g": 660,  # E4
    "h": 698,  # F4
    "j": 784,  # G4
    "k": 880   # A5
}


def wave(note, duration=1):
    """ Base method for generating basic wave data that must then be transformed into specialized waveforms """

    frequency = notes[note]
    samp_rate = 44100
    n_data = duration * samp_rate
    time = np.arange(0, n_data).T / samp_rate
    init_phase = np.pi / 2

    return frequency, time, init_phase


def sine(note, amplitude):
    """ Generates a sine wave at given note and with given amplitude """

    frequency, time, init_phase = wave(note)
    return amplitude * np.cos(2 * np.pi * frequency * time + init_phase)


def square(note, amplitude):
    """ Generates a square wave at given note and with given amplitude """

    frequency, time, init_phase = wave(note)
    return amplitude * signal.square(2 * np.pi * frequency * time + init_phase, duty=0.5)


def saw(note, amplitude):
    """ Generates a saw wave at given note and with given amplitude """

    frequency, time, init_phase = wave(note)
    return amplitude * signal.sawtooth(2 * np.pi * frequency * time + init_phase)
