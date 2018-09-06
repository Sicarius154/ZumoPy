#!/usr/bin/env python3
import math
import random
from serialconnection import ZumoConnection
from util.logging import Logging
from instructions import Instructions
from zumosensors import ZumoSensors
class Zumo32u4:
    def __init_(self, name="Zumo32u4", port="/dev/tty/ACM0"):
        self.name = name
        self.max_speed = 100 # This is the maximum speed allowed for the zumo. It works as a percentage
        self.logger = Logging(f"./logs/{name}")
        self.connection = ZumoConnection(self.logger, port)
        self.logger.log_info("Created Zumo32u4 instance")
        self.sensors = ZumoSensors()

    def _set_right_motor_speed(self, speed):
        """
            Sets the speed of the right motor
            :param speed: The speed for the motor. Between 0 and 100. Acts as a percentage
        """
        instruction = "Instructions.SET_RIGHT_MOTOR_SPEED"
        speed = f"{speed};"#This will grab the value
        instruction = f"{instruction}{speed};"
        self.connection.send_instruction(instruction)

    def _set_left_motor_speed(self, speed):
        """
            Sets the speed of the left motor
            :param speed: The speed for the motor. Between 0 and 100. Acts as a percentage
        """
        instruction = "Instructions.SET_LEFT_MOTOR_SPEED"
        speed = f"{speed};"#This will grab the value
        instruction = f"{instruction}{speed};"
        self.connection.send_instruction(instruction)

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

    def turn_right(self, angle, speed):
        """
            Will make the zumo rotate to the right by moving only the right motor.
            :param angle: The angle to turn. Taken as an integer between 0 and 360.
            :param speed: How fast the turn should be completed. Between 0 and 100.
        """
        if angle < 0 or angle > 360:
            self.logger.log_warn(f"Receieved an angle of {angle} in turn_right. Not valid. Ignoring instruction")

    def turn_left(self, angle, speed):
        """
            Will make the zumo rotate to the left by moving only the left motor.
            :param angle: The angle to turn. Taken as an integer between 0 and 360.
            :param speed: How fast the turn should be completed. Between 0 and 100.
        """
        if angle < 0 or angle > 360:
            self.logger.log_warn(f"Receieved an angle of {angle} in turn_right. Not valid. Ignoring instruction")
        pass
