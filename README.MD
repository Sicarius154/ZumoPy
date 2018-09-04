# ZumoPy
ZumoPy is a librry designed to pair the Zumo 32u4 and a rapsberry pi microcomputer. The code is designed with the inclusion of a raspberry pi on the zumo itself in mind.

## How it works
There are two components. The Pi side, and the Zumo side. The Zumo component will be run on the Zumo itself, and will contain all of the code necesary for manipulating and controlling the zumo. This code will simply listen for commands and act upon them.

The Pi side is what the user will see. It will contain many high level functions to facilitate the controlling of the Zumo. All error checking, data validation and so forth is done here. With minimal logic required on the Zumo

# Instructions and communication

## Communication
The library is designed to use the serial connection found on the raspberry pi and the Zumo. Data transfer is limited to X bits per second.

## Instructions
The ZumoPy interface works with a limited instruction length, to allow for simplicity and minimal data transfer. Due to the limitations of serial, and ensuring data can be transfered at a reliable rate instructions are kept short and easy to parse. Below is a list of instructions that the Zumo will accept and ackknowledge. Any incorrect instructions are simply **discarded and ignored**. The '^' character denotes an unused char in the instruction string
The first character of an instruction denotes the type of instruction:
0 = Get sensor data (Sending these instructions tell the Zumo to send the most recent sensor data back)
1 = Set motors (Used for movement and turning)
|Instruction|Usage                                      |
|-----------|-------------------------------------------|
|000^^^^^   |Get the proximity sensor data              |
|010^^^^^   |Get the line sensor data                   |
|011^^^^^   |Get both the line and proximity sensor data|
|100YY^^^   |Set the right motor to speed Y.Y*100       |
|110YY^^^   |Set the left motor to speed Y.Y*100        |

The Pi will *not* take instructions. It will simply receive data from the sensors. In the future it will also accept status codes. Below is the format for sensor data.
