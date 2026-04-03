import pytest

class Test_Reading:
    """Testing all the methods related to reading messages from the serial communication."""
    
    def test_recognize_start_byte(byte, is_start_sequence):
        pass
    
    def test_recognize_message_type(byte, message_type):
        pass
    
    def test_recognize_message_length(byte, length):
        pass
    
    def test_read_message_from_bytes(byte_sequence, message):
        pass
    
    def test_recognize_check_sum(message, byte):
        pass

    def test_recognize_wrong_check_sum(message, is_correct):
        pass