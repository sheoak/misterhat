"""misterhat_server.py.

Main class for misterhat server.

TODO: plugin system

"""
import time

import pyttsx3  # voice synthesis

from misterhat import misterhat_module


class MisterhatServer:
    """Main class to run the server.

    """
    _modules = {}  # instances of modules

    config = {
        'SILENT': False,  # do no use vocal synthesis if True
        'ALERT_DELTA': 60,  # delay before triggering the same alert
        'USE_EMULATOR': False,  # sense-hat emulator
        'VOICE_SPEED': 100,  # voice synthesis speed in percent
        'LIST_MODULES': ('temp')  # list of installed modules
    }

    def __init__(self, config={}):

        # merge our configuration
        self.config = {**self.config, **config}

        self._init_sensehat()
        self._init_vocal()
        self._init_modules()

    def _init_modules(self):
        """
        Initialize the modules objects

        """
        for module in self.config['LIST_MODULES']:
            modname = 'MisterhatModule' + module.title()
            modfunc = getattr(misterhat_module, modname)
            self._modules[module] = modfunc(self)

    def _init_sensehat(self):
        """
        Initialize the sense-hat.

        Note that this might be an emulator.
        """

        if self.config['USE_EMULATOR']:
            from sense_emu import SenseHat
        else:
            from sense_hat import SenseHat

        # init sense-hat
        self.sense = SenseHat()

    def _init_vocal(self):
        """
        Initialize the vocal synthetizer.

        """
        # init voice synthesis
        if not self.config['SILENT']:
            self.voice = pyttsx3.init()
            self.voice.setProperty('rate', self.config['VOICE_SPEED'])

    def event(self, data):
        """Called by the module when an event happens

        """
        self.sense.set_pixels(data['emoji'])

        message = data['message'] % {'value': data['value']}
        print(message)

        if not self.config['SILENT']:
            self.voice.say(message)
            self.voice.runAndWait()

        time.sleep(1)

    def run(self):
        """Run the observation of the sense-hat

        """
        while True:
            for module in self.config['LIST_MODULES']:
                self._modules[module].analyze()
