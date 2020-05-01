from pyfiglet import Figlet
from synth import Synth
from gui import GUI


if __name__ == '__main__':

    # print welcome screen
    f = Figlet(font='slant')
    print(f.renderText('7SYNTH'))
    print("7SYNTH ULTRA MEGA-XTREME: ULTIMATE EDITION. Program has launched in a separate window - enjoy!")

    # initialize synth
    synth = Synth()

    # initialize and run gui
    gui = GUI(synth)
    while not gui.closed:
        gui.update()
