
=========
Misterhat
=========

This is just a little experiment with the sense-hat emulator from Raspberry-pi.
You can also use it with the actual sense-hat.


Install
=======

    pip install -r requirements


Usage
=====

   from misterhat import MisterhatServer

   config = {
       'SILENT': False,  # default value, use vocal synthesis
       'VOICE_SPEED': 98,  # speech speed
       'USE_EMULATOR': True,  # use the sense-hat emulator
       'LIST_MODULES': (
           'shake',
           'temp',
           'humidity',
           'pressure'
       )
   }
   server = MisterhatServer(config)
   server.run()
