"""misterhat_server.py.

Main class for misterhat server.

TODO: plugin system

"""

import pyttsx3  # voice synthesis

from misterhat import misterhat_module


class MisterhatServer:
    """Main class to run the server.

    """
    list_modules = ('temp')
    modules = {}

    def __init__(self, conf):

        # try:
        self.conf = conf
        self.list_modules = conf.LIST_MODULES
        # except NoModuleConfigured:
        # raise Exception('No module has been configured')

        self._init_sensehat()
        self._init_vocal()
        self._init_modules()

    def _init_modules(self):
        """
        Initialize the modules objects

        """
        for module in self.list_modules:
            modname = 'MisterhatModule' + module.title()
            modfunc = getattr(misterhat_module, modname)
            self.modules[module] = modfunc(self.sense, self.engine)

    def _init_sensehat(self):
        """
        Initialize the sense-hat.

        Note that this might be an emulator.
        """

        if getattr(self.conf, 'USE_EMULATOR', False):
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
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', self.conf.VOICE_SPEED)

    def run(self):
        """Run the observation of the sense-hat

        """

        while True:
            for module in self.list_modules:
                self.modules[module].analyze()
