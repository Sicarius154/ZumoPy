import serial
import time
from exceptions.InvalidInstruction import InvalidInstruction
from exceptions.connectionError import ConnectionError
from ..instructions import Instructions

class ZumoConnection:
    def __init__(self, logger, port, baud_rate=19200, timeout=5):
        """
            Initialize the connection. Check to ensure the connection is functional
            :param logger: An instance of the logger utility
            :param port: The port to use for serial connection
            :param baud_rate: The baud rate for the connection
            :param timeout: The timeout value for the serial connection.
        """
        self.logger = logger
        self.logger.log_info("Created Serial Connection to Zumo")
        slf.baud = baud_rate
        self.sensor_thread = None #Object to interact with the thread that will listen for sensor data
        self.connection = self.connect(port, baud_rate, timeout)
        connected_ok = self._check_connection()
        if connected_ok:
            pass
        else:
            self.logger.log_warn(f"Could not connect to Zumo. Params were:\
            Port: {port}\
            Baud rate: {baud_rate}\
            Timeout: {timeout}")
            raise ConnectionError("Error connecting to Zump")

    def _check_connection(self):
            """
                Checks the connection is open correctly. If the connection has been opened succesfuly the Zumo should have
                begun sending data back to the Zumo instance.
            """
            pass
    def send_instruction(self, inst):
        """
            Sends an instruction to the Zumo over a serial connection
            :param ins: The 8-char long instruction.
        """
        self.logger.log_info(f"Received instruction {inst}")
        if(_check_inst_validity(inst)):
            data = get_bytes(inst)
            self._send(data)

    def _connect(self, port, baud, timeout):
        """
            Will attempt to connect to the Zumo using the params supplied.
            :param port: The port to connect to
            :param baud: The baudrate of the connection
            :param timeout: The timeout for the connection
        """
        #Connect and send the connect instruction
        #TODO: Look into using parity bits
        con = serial.Serial(port, baud, timeout=timeout)
        con.inner_byte_timeout = 0.5 #The time allowed between bytes being sent in a message
        con.send_instruction(self._get_bytes(Instructions.CONNECT)) #We send this now so the Zumo can instantly start sending sensor data
        return con

    def disconnect(self):
        """
            Will end the serial connection and tell the Zumo to cease all operation.
        """
        pass
    def _sensor_data_received(self, data):
        """
            To be called asynchronously when sensor data is received by the sensor_thread. This will set the Zumo object
            sensor data to this instance
        """
        pass

    def _check_inst_validity(self, inst):
        """
            Will check the validity of an instruction by checking a handful of criteria such as the length of an instruction,
            the value of certain characters etc. The majority of checking should have been done before hand. This will not
            check that the speed for setting motors is correct for example; just the format of the instruction
            :param inst: The instruction
            :return: Whether the instruction is OK
        """
        if inst[len(inst)-1] != ";":
            inst = inst+";" #ensure the instruction is properly terminated
            self.logger.log_error(f"Instruction not properly terminated. Inst was {inst}")
            raise InvalidInstruction(f"{inst} is not a valid instruction")
            return False
        return True #if none of the if statements were triggered, all is good

    def _send(self, data):
        """
            Send data across the serial connection
            :param data: The data to send
        """
        size = None #TODO: get size of inst
        self.connection.write(data)
        self.logger.log_info("Sent {size} bytes of data")

    def _get_bytes(self, string):
        """
            Converts a string instruction into bytes
            :param string: The instruction
            :return: The string given as bytes
        """
        return bytes(string, "utf-8")
