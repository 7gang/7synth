import sounddevice as sd
import waves
import numpy as np

class Synth:

    def __init__(self):
        self.waveform = 'SINE'  # can also be "SQUARE" or "SAW"
        self.low_pass = 0.0     # level of low pass filter
        self.band_pass = 0.0    # level of band pass filter
        self.volume = 0.5       # default volume
        self.key = 'a'          # default note
        self.wave_map = {       # all the waves
            'SINE': waves.sine,
            'SQUARE': waves.square,
            'SAW': waves.saw
        }

    def set(self, play_preview, **kwargs):
        """ Sets playback variables, restarting playback if a value is changed """

        settings_changed = False
        for i in range(len(kwargs)):
            name = str(list(kwargs.keys())[i])
            value = kwargs[name]
            # set new class variable value if changed
            variable = self.__dict__[name]
            if variable != value:
                settings_changed = True
                self.__dict__[name] = value
                print("updated %s from %s to %s" % (name, variable, value))

        # update playback if playback variables changed
        if play_preview and settings_changed:
            self.play()

    def play(self, key=None):
        """ Starts playback """
        # replace key and stop playback before starting it again
        if key:
            if key not in waves.notes:  # cancel method if pressed key is not supported
                return
            self.key = key
        self.stop()
        """Generating a signal"""
        signal = self.wave_map.get(self.waveform)(self.key, self.volume / 10)
        """Applying a filter fo the signal if the filter is turned on(>0)"""
        if self.low_pass > 0:
            signal = self.lowpass(signal, self.low_pass)
        """if self.band_pass > 0:
            signal = #bandpass processing"""
        # play sound
        sd.play(signal)
        print("playing note in key %s with waveform %s, low pass %s, and band pass %s"
              % (self.key, self.waveform, self.low_pass, self.band_pass))

    def stop(self):
        """ Stops playback. This method is called preemptively, even when nothing is playing """

        sd.stop()
    """Filtering section"""
    def lowpass(self, signal, cutoff):
        filtersignal = np.zeros_like(signal)
        dt = 1/44100 #calculating the descrete time
        tau = 1/cutoff
        a = dt / tau
        filtersignal[0] = a * signal[0]
        for i in range(1, 44100 - 1):
             filtersignal[i] = filtersignal[i - 1] + a * (signal[i] - filtersignal[i - 1])
        return filtersignal
