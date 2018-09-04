import serial
class ZumoConnection:
    def __init__(self, logger):
        self.logger = logger
        self.connection = serial.Serial("/dev/tty/ACM0", 9600)
        self.logger.log_info("Created Serial Connection to Zumo")

    def send_instruction(self, inst):
        """
            Sends an instruction to the Zumo over a serial connection
            :param ins: The 8-char long instruction.
        """

        self.logger.log_info(f"Received instruction {inst}")
    def connect(self):
        pass
    def disconnect(self):
        pass
    def sensor_data_received(self, data):
        pass

    def check_inst_validity(self, inst):
        """
            Will check the validity of an instruction by checking a handful of criteria such as the length of an instruction,
            the value of certain characters etc. The majority of checking should have been done before hand. This will not
            check that the speed for setting motors is correct for example; just the format of the instruction
            :param inst: The instruction
            :return: Whether the instruction is OK
        """
        if len(inst) != 8:
            return False
        if not inst[0] in [0, 1]:
            return False
        return True #if none of the if statements were triggered, all is good

    def send(self, data):
        """
            Send data across the serial connection
            :param data: The data to send
        """
        data = get_bytes(data)
        self.connection.write(data)

    def get_bytes(self, string):
        """
            Converts a string instruction into bytes
            :param string: The instruction
            :return: The string given as bytes
        """
        return bytes(string, "utf-8")    
