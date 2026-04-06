from enum import Enum

class DigitalPin(Enum):
    HIGH = 1
    LOW = 0
    
class MessageType(Enum):
    WRITE_DIGITAL = 0x01
    READ_DIGITAL = 0x02
    DIGITAL_VALUE_RESPONSE = 0x03
    WRITE_ANALOGUE = 0x04
    READ_ANALOGUE = 0x05
    ANALOGUE_VALUE_rESPONSE = 0x06
    WRITING_CONFIRMATION = 0x07
    RESET = 0x10