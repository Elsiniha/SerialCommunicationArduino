import serial
import struct

from TypeClasses import DigitalPin 

class SerialCommunication:
    def __init__(self, com_port: str, baud: int, name: str):
        self.com_port = com_port
        self.baud = baud
        self.name = name
        
        self.serial = serial.Serial()
        
        self.start_byte = b'\xAA'
    
    def connect(self,):
        """Establishing the connection to the serial port."""
        try:
            self.serial = serial.Serial(self.com_port, self.baud)
            
        except Exception as e:
            raise ConnectionError(f"Could not connect to the Serial port {self.com_port}. Caught exception {e}")
    
    def disconnect(self, ):
        """Closing the connection to the serial port."""
        self.serial.close()
    
    # def calculate_check_sum(self, byte_sequence: list[bytes]):
    #     """Calculating the checksum of the byte sequence to verify the full payload was transmitted."""
    #     check_sum = 0
        
    #     for byte in byte_sequence:
    #         byte_value = struct.unpack('<i', byte)
    #         check_sum += byte_value
        
    #     return check_sum
    
    
    
    def calculate_check_sum(self, data: bytes):
        """Calculating the checksum of the byte sequence to verify the full payload was transmitted."""
        return sum(data) % 256
    
    def transform_message_to_byte(message) -> bytes:
        """Transforming the message into the byte sequence."""
        if type(message) == type(int):
            message_byte = struct.pack('<i', message)
            
        if type(message) == type(float):
            message_byte = struct.pack('<f', message)
        
        return message_byte

    def write_digital_pin_message(self, pin_number: int, message: DigitalPin) -> list[bytes]:
        """Putting together the message for writing a digital pin"""
        message_type_byte = b'\x01'
        
        pin_number_byte = bytes([pin_number])
        message_byte = bytes([message.value])
        message_len_byte= bytes([len(message_byte)])
        
        message_full_byte = (
            self.start_byte +
            message_type_byte +
            message_len_byte +
            pin_number_byte +
            message_byte
            )
        
        check_sum = bytes([self.calculate_check_sum(message_full_byte)])
        
        message_full_byte = message_full_byte + check_sum
        
        print("The digital write message is:", message_full_byte)
        
        return message_full_byte
    
    def write_analogue_pin_message(self, pin_number: int, message: int) -> bytes:
        """Putting together the message to write an analogue value to one of the pins"""
        if message < 0 or message > 1024:
            raise ValueError("The Analogue values must be in the range of 0 to 1023.")
                
        message_type_byte = b'\x04'
        
        pin_number_byte = bytes([pin_number])
        message_byte = struct.pack('<H', message)
        message_len_byte= bytes([len(message_byte)])
        
        message_full_byte = (
            self.start_byte +
            message_type_byte +
            message_len_byte +
            pin_number_byte +
            message_byte
            )
        
        check_sum = bytes([self.calculate_check_sum(message_full_byte)])
        
        message_full_byte = message_full_byte + check_sum
        
        print("The analogue write message is:", message_full_byte)
        
        return message_full_byte
    

if __name__ == "__main__":
    ser = SerialCommunication("COM3", 9600, "Sandbox")
    ser.write_digital_pin_message(12, DigitalPin.HIGH)
    
    ser.write_analogue_pin_message(26, 1001)
    ser.write_analogue_pin_message(22, 2002)
    
        
        
    
        
    
    
    