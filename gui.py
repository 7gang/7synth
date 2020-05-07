import PySimpleGUI as sg


def build():
    # all the stuff inside the GUI window
    return [[sg.Image('./logo.png')],
            [sg.Text('----------------------------------------------------------------------------')],
            [sg.Text("WAVEFORM")],
            [sg.Listbox(['SINE', 'SQUARE', 'SAW'],
                        enable_events=True,
                        size=(None, 3),
                        auto_size_text=True,
                        default_values='SINE',
                        key='wave'),
             sg.Checkbox('Play preview audio', default=True, key='tick')],
            [sg.Text('----------------------------------------------------------------------------')],
            [sg.Text("LOW PASS FILTER")],
            [sg.Slider(range=(0, 20000), orientation='h', size=(34, 20), default_value=0, resolution=50,
                       enable_events=True, key='low')],
            [sg.Text("BAND PASS FILTER")],
            [sg.Slider(range=(0.0, 14000.0), orientation='h', size=(34, 20), default_value=0, resolution=50,
                       enable_events=True, key='ban')],
            [sg.Text("VOLUME")],
            [sg.Slider(range=(0.0, 1.0), orientation='h', size=(34, 20), default_value=.5, resolution=.1,
                       enable_events=True, key='vol')],
            [sg.Text('----------------------------------------------------------------------------')],
            [sg.Button("QUIT", key='QUIT'),
             sg.Text("Press keys A,S,D,...,K to play")]]


class GUI:
    """ Manages the Graphical User Interface of the application, invoking Synth.py """

    def __init__(self, synth):
        sg.theme('DarkAmber')  # add a touch of color

        # create the Window
        layout = build()
        self.window = sg.Window('7SYNTH ULTRA MEGA-XTREME: ULTIMATE EDITION', layout,
                                return_keyboard_events=True,
                                use_default_focus=False,
                                icon='icon.ico')
        self.window.finalize()  # dunno if this is strictly needed, seemed to work fine without

        # create other class variables
        self.closed = False
        self.synth = synth

    def update(self):
        """ Updates the GUI, invoking Synth """

        # process "events" and get the "values" of the inputs
        event, values = self.window.read()
        low_pass_slider = values['low']
        ban_pass_slider = values['ban']
        volume_slider = values['vol']
        waveform = values['wave'][0]
        play_preview_audio = values['tick']

        # pass values to Synth
        self.synth.set(play_preview_audio,
                       waveform=waveform,
                       low_pass=low_pass_slider,
                       band_pass=ban_pass_slider,
                       volume=volume_slider)

        # parse GUI input
        if event in ("QUIT", None):
            print("Quiting 7SYNTH ULTRA MEGA-XTREME: ULTIMATE EDITION...")
            return self.close()
        if len(event) == 1:
            self.synth.play(event[0])

    def close(self):
        """ Closes the GUI, ending the program """

        self.window.close()
        self.closed = True
