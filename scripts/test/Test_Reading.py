import pytest

from scripts.SerialComPy.MessageType import MessageType


class Test_Reading:
    """Testing all the methods related to reading messages from the serial communication."""
    
    @pytest.mark.parametrize("byte, is_start_sequence", 
                             [(0b10101010, True), 
                              (0b11001100, False),
                              (0b01010101, False)])
    def test_recognize_start_byte(self, byte, is_start_sequence):
        if byte == 0b10101010:
            assert is_start_sequence == True
        else:
            assert is_start_sequence == False
    
    @pytest.mark.parametrize("byte, message_type",
                             [(0x01, MessageType.WRITE_DIGITAL),
                              (0x02, MessageType.READ_DIGITAL),
                              (0x10, MessageType.RESET),
                              (0xA0, ValueError)])
    def test_recognize_message_type(self, byte, message_type):
        if byte in MessageType:
            return MessageType(byte).name
             
        else:
            return ValueError("Has is invalid message type")
            
    
    def test_read_message_from_bytes(self, byte_sequence, message):
        pass
    
    def test_recognize_check_sum(self, message, byte):
        pass

    def test_recognize_wrong_check_sum(self, message, is_correct):
        pass