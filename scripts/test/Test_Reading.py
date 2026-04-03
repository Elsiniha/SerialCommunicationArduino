import pytest

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
    
    
    def test_recognize_message_type(self, byte, message_type):
        pass
    
    def test_recognize_message_length(self, byte, length):
        pass
    
    def test_read_message_from_bytes(self, byte_sequence, message):
        pass
    
    def test_recognize_check_sum(self, message, byte):
        pass

    def test_recognize_wrong_check_sum(self, message, is_correct):
        pass