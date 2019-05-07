"""misterhat_module.py.

"""
import time
import operator
from datetime import datetime, timedelta

from misterhat import emoji


class MisterhatModule:

    """Abstract class for misterhat modules

    """

    low = {}
    high = {}

    # TODO: configuration
    def __init__(self, sense, engine):
        self.sense = sense
        self.engine = engine
        self.alert_delta = timedelta(seconds=600)

    def compare(self, field, value):
        """Compare the value from the configuration with the current value

        This will memorize the last date the state was check
        to avoid repeating the same message too often.

        """

        # dynamic comparison
        ope = operator.gt if field == 'high' else operator.lt
        field_inv = 'low' if field == 'high' else 'high'

        conf = getattr(self, field)

        # we divide the condition for readability
        if ope(conf['value'], value):
            return False

        if ('lastcheck' in conf and
                (datetime.now() - self.alert_delta) < conf['lastcheck']):
            return False

        conf['lastcheck'] = datetime.now()
        getattr(self, field_inv)['lastcheck'] = datetime(1970, 1, 1, 0, 0)
        return True

    def analyze(self):
        """ Run the evaluation for the requested module

        """

        value = self.value()

        # analyze for low and high values
        for field in ('low', 'high'):
            conf = getattr(self, field)
            if 'value' in conf and self.compare(field, value):
                self.sense.set_pixels(conf['emoji'])
                self.engine.say(conf['msg'] % {'value': value})
                self.engine.runAndWait()
                time.sleep(1)

    def value(self):
        """Must be implemented in the submodule

        """
        raise NotImplementedError("Not implemented")


class MisterhatModuleHumidity(MisterhatModule):
    """Must be implemented in the humidity

    """
    low = {
        'value': 10,  # in percent
        'msg': "It's so dry, did you left me near the heater, kid?",
        'emoji': emoji.EMOJI_HUMIDITY_LOW,
    }
    high = {
        'value': 80,  # in percent
        'msg': "It's humid in there, %(value)d percent, oh my circuits…",
        'emoji': emoji.EMOJI_HUMIDITY_HIGH,
    }

    def value(self):
        """Return the current humidity value on the sense-hat

        """
        return self.sense.get_humidity()


class MisterhatModuleTemp(MisterhatModule):
    """Module class for the temperature

    """
    low = {
        'value': 15,
        'msg': "I'm freezing, help me! %(value)d degrees only!",
        'emoji': emoji.EMOJI_TEMP_LOW
    }
    high = {
        'value': 22,
        'msg': "Don't forget to drink, it's hot today, %(value)d degrees !",
        'emoji': emoji.EMOJI_TEMP_HIGH
    }

    def value(self):
        """Return the current temperature value on the sense-hat

        """
        return self.sense.get_temperature()


class MisterhatModulePressure(MisterhatModule):
    """Module class for the pressure.

    """
    low = {
        'value': 1009.144,  # in mbar
        'msg': "I think it's gonna rain, please protect me…",
        'emoji': emoji.EMOJI_PRESSURE_LOW
    }
    high = {
        'value': 1022.689,  # in mbar
        'msg': "It's gonna be a beautiful day!",
        'emoji': emoji.EMOJI_PRESSURE_HIGH
    }

    def value(self):
        """Return the current pressure value on the sense-hat

        """
        return self.sense.get_pressure()


class MisterhatModuleShake(MisterhatModule):
    """Module class for the accelerometer.

    """
    high = {
        'value': 3,
        'msg': "Hey! Be gentle, kiddo!",
        'emoji': emoji.EMOJI_SHAKE,
    }

    def value(self):
        """Return the current shaking value on the sense-hat

        """
        acceleration = self.sense.get_accelerometer_raw()
        return (abs(acceleration['x']) + abs(acceleration['y']) +
                abs(acceleration['z']))
