import math
import random
from .SerialConnection import ZumoConnection
from util.logging import Logging
from instructions import Instructions
class Zumo32u4:
    def __init_(self, name="Zumo32u4"):
        self.name = name
        self.max_speed = 4.0 # This is the maximum speed allowed for the zumo, any values passed that exceed this are rounded down to this value.
        self.logger = Logging(f"./logs/{name}")
        self.connection = ZumoConnection(self.logger)
        self.logger.log_info("Created Zumo32u4 instance")

    def _set_right_motor_speed(self, speed):
        instruction = "Instructions.SET_RIGHT_MOTOR_SPEED"
        speed = f"{speed[0]}{speed[2]};"#This will grab the value
        instruction = f"{instruction}{speed};" #is now of format XXXYY--- where XXX = inst YY = speed --- = unused
        self.connection.send_instruction(instruction)

    def _set_left_motor_speed(self, speed):
        pass

    def move_forward(self, speed):
        """
            Will make the zumo move forward. Does this by taking a value (the speed) and sets both
            left and right motors to this speed.
            :param speed: Speed for the zumo. Expected as a float.
        """
        speed = float(speed)
        if speed > self.max_speed:
            self.logger.log_warn(f"Received speed of {speed} in move_forward. Rounded down to {self.max_speed}")
            speed = self.max_speed
        self._set_left_motor_speed(speed)
        self._set_right_motor_speed(speed)

    def move_backward(self, speed):
        """
            Will make the zumo move backward. Does this by taking a value (the speed) and sets both
            left and right motors to this speed.
            :param speed: Speed for the zumo, will be taken as a negative value. Expected as a float.
        """
        if speed > self.max_speed:
            self.logger.log_warn(f"Received speed of {speed} in move_backward. Rounded down to {self.max_speed}")
            speed = self.max_speed
        self._set_left_motor_speed(-speed)
        self._set_right_motor_speed(-speed)

    def turn_right(self, angle):
        """
            Will make the zumo rotate to the right by moving only the right motor.
            :param angle: The angle to turn. Taken as an integer between 0 and 360.
        """
        if angle < 0 or angle > 360:
            self.logger.log_warn(f"Receieved an angle of {angle} in turn_right. Not valid. Ignoring instruction")
        pass

    def turn_left(self, angle):
        """
            Will make the zumo rotate to the left by moving only the left motor.
            :param angle: The angle to turn. Taken as an integer between 0 and 360.
        """
        if angle < 0 or angle > 360:
            self.logger.log_warn(f"Receieved an angle of {angle} in turn_right. Not valid. Ignoring instruction")
        pass
