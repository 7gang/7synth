import sounddevice as sd
from waves import sine, square, saw


class Synth:

    def __init__(self):
        self.waveform = 'SINE'  # can also be "SQUARE" or "SAW"
        self.low_pass = 0.0     # level of low pass filter
        self.band_pass = 0.0    # level of band pass filter
        self.volume = 0.5       # default volume
        self.key = 'a'          # default note
        self.waves = {          # all the wavezzz
            'SINE': sine,
            'SQUARE': square,
            'SAW': saw
        }

    def set(self, preview, **kwargs):
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
        if preview and settings_changed:
            self.play()

    def play(self, key=None):
        """ Starts playback """

        # replace key and stop playback before starting it again
        if key:
            self.key = key
        self.stop()

        # play sound
        sd.play(self.waves.get(self.waveform)(self.key, self.volume / 10))

        print("playing note in key %s with waveform %s, low pass %s, and band pass %s"
              % (self.key, self.waveform, self.low_pass, self.band_pass))

    def stop(self):
        """ Stops playback. This method is called preemptively, even when nothing is playing """

        sd.stop()
