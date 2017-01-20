import serial
from up.base_started_module import BaseStartedModule



class SerialProvider(BaseStartedModule):
    BAUD_RATE_DEFAULT = 9600

    def __init__(self, port, baud_rate=BAUD_RATE_DEFAULT):
        super().__init__()
        self.__serial_port = port
        self.__serial = serial.Serial()
        self.__serial.baudrate = baud_rate

    def _execute_initialization(self):
        pass

    def _execute_start(self):
        pass

    def _execute_stop(self):
        pass

    def load(self):
        return True

    @property
    def serial_port(self):
        return self.__serial_port
