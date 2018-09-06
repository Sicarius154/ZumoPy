import serial
from exceptions.InvalidInstruction import InvalidInstruction
class ZumoConnection:
    def __init__(self, logger, port):
        self.logger = logger
        self.connection = serial.Serial(port, 9600)
        self.logger.log_info("Created Serial Connection to Zumo")

    def send_instruction(self, inst):
        """
            Sends an instruction to the Zumo over a serial connection
            :param ins: The 8-char long instruction.
        """
        self.logger.log_info(f"Received instruction {inst}")
        data = get_bytes(inst)
        self._send(data)


    def connect(self):
        pass
    def disconnect(self):
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
            self.logger.log_warn(f"Instruction not properly terminated. Terminating. Inst was {inst}")
        if not inst[0] in [0, 1]:
            self.logger.log_error("Invalid instruction")
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
