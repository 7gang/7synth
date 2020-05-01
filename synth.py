#import sounddevice as sd


class Synth:

    def __init__(self):
        self.waveform = 'SINE'  # can also be "SQUARE" or "SAW"
        self.low_pass = 0.0
        self.band_pass = 0.0
        self.volume = 0.5
        self.key = 'c'

    def set(self, **kwargs):
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
        # update playback if playing
        if settings_changed:
            self.play()

    def play(self, key=None):
        """ Starts playback """

        # save key
        if not key:
            key = self.key
        self.key = key
        # stop before starting
        self.stop()

        # TODO: play note in the given key continuously...

        print("playing note in key %s with waveform %s, low pass %s, and band pass %s"
              % (key, self.waveform, self.low_pass, self.band_pass))

    def stop(self):
        """ Stops playback. This method is called preemptively, even when nothing is playing """
        # TODO:                                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ must be able to handle this

        # TODO: stop playing note...
        pass
