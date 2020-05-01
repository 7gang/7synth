import PySimpleGUI as sg


def build():
    # all the stuff inside the gui window
    return [[sg.Text("Press a key to play a note...")],
            [sg.Text("WAVEFORM")],
            [sg.Listbox(['SINE', 'SQUARE', 'SAW'],
                        enable_events=True,
                        size=(None, 3),
                        auto_size_text=True,
                        default_values='SINE',
                        key='wave')],
            [sg.Text("LOW PASS FILTER")],
            [sg.Slider(range=(0, 1), orientation='h', size=(34, 20), default_value=0, resolution=.1,
                       enable_events=True, key='low')],
            [sg.Text("BAND PASS FILTER")],
            [sg.Slider(range=(0.0, 1.0), orientation='h', size=(34, 20), default_value=0, resolution=.1,
                       enable_events=True, key='ban')],
            [sg.Text("VOLUME")],
            [sg.Slider(range=(0.0, 1.0), orientation='h', size=(34, 20), default_value=.5, resolution=.1,
                       enable_events=True, key='vol')],
            [sg.Text("", size=(18, 1), key='text')],
            [sg.Button("QUIT", key='QUIT')]]


class GUI:

    def __init__(self, synth):
        sg.theme('DarkAmber')  # add a touch of color

        # create the Window
        layout = build()
        self.window = sg.Window('7SYNTH ULTRA MEGA-XTREME: ULTIMATE EDITION', layout,
                                return_keyboard_events=True,
                                use_default_focus=False)
        self.window.finalize()  # dunno if this is strictly needed, seemed to work fine without

        # create other class variables
        self.closed = False
        self.synth = synth

    def update(self):
        """ Updates the GUI, invoking Synth """

        # event Loop to process "events" and get the "values" of the inputs
        event, values = self.window.read()
        text_elem = self.window['text']
        low_pass_slider = values['low']
        ban_pass_slider = values['ban']
        volume_slider = values['vol']
        waveform = values['wave'][0]
        # print("low: %s, band: %s" % (low_pass_slider, band_pass_slider))
        # print(event)
        self.synth.set(waveform=waveform,
                       low_pass=low_pass_slider,
                       band_pass=ban_pass_slider,
                       volume=volume_slider)
        if event in ("QUIT", None):
            print("Quiting 7SYNTH ULTRA MEGA-XTREME: ULTIMATE EDITION...")
            return self.close()
        if len(event) == 1:
            self.synth.play(event[0])
            text_elem.update(value='%s - %s' % (event, ord(event)))
        if event is not None:
            text_elem.update("DEBUGGING: %s" % event)
            pass

    def close(self):
        """ Closes the GUI, ending the program """

        self.window.close()
        self.closed = True
