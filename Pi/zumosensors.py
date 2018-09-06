class ZumoSensors:
    def __init__(self):
        pass

    def get_line_sensors(self):
        """
            Returns an array containing just the line sensor data
            :returns: An array of sensor values
        """
        pass

    def get_prox_sensors(self):
        """
            Returns an array containing just the proximity sensor data
            :returns: An array of sensor values
        """
        pass

    def get_sensors(self):
        """
            Returns an array matching the array format used to set sensor data.
            :returns: An array of sensor values
        """
        pass

    def set_sensor_data(self, data):
        """
            Sets the sensor data for this instance and updates the last_updated timestamp.
            :param data: An array following the format found in the documentation.
        """
        pass

    def get_last_updated(self):
        """
            Gets the last timestamp of when the sensors were updated. This is NOT the time that the Zumo sent the data
            back but the time at which the new values were set in this class
            :returns: UNIX timestamp of last update
        """
        pass
