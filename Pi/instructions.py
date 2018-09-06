"""
    This file contains the list of instruction codes to be used.
    Information on how instructions work can be found in the docs
"""

class Instructions(Enum):
    CONNECT = "C"
    DISCONNECT = "D"
    SET_LEFT_MOTOR_SPEED = "SL"
    SET_RIGHT_MOTOR_SPEED = "SR"
    SET_TURN_RIGHT = "TR"
    SET_TURN_LEFT = "TL"
    GET_LINE_SENSORS = "GL"
    GET_PROXIMITY_SENSORS = "GP"
    GET_BOTH_SENSORS = "GB"
