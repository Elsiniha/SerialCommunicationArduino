# Communication Protocol

To communicate with the Arduino's pins we have a script running on the Arduino that continuously waits for a request from the main script on the computer. The communication medium are sequences of bytes that have a very specific structure:

```
[Start Sequence Byte] -> [Message Type Byte] -> [Message Length Byte] -> [...][Payload][...] -> [Check Sum Byte]
```

- Start Sequence Byte: Byte containing the start sequence signaling the start of a message. The start sequence used in this project is **0xAA** which translates to the Bit-Sequence of **10101010**
- Message Type Byte: Type of message. The message can be one of the following types:

| Message Type: | Byte Value: | Info: |
|---|---|---|
| Write Digital | 0x01 | Sending a write request for a digital pin to the Arduino and awaiting a Confirmation response |
| Read Digital | 0x02 | Sending a reading request for the value of a digital pin to the Arduino and awaiting the value response | 
| Digital Value Response | 0x03 | Response to a read request for the value of a digital pin |
| Write Analogue | 0x04 | Sending a write request for a analogue pin to the Arduino and awaiting a Confirmation response |
| Read Analogue |  0x05 | Sending a reading request for the value of a analogue pin to the Arduino and awaiting the value response |
| Analogue Value Response | 0x06 | Response to a read request for the value of a analogue pin |
| Writing Confirmation | 0x07 | Confirmation that a writing request has been processed successfully |
| Write Reset | 0x10 | Writing the reset pin of the Arduino to reset the board | 
| Write String | 0x20 | |
| Read String | 0x21 | |
| String Value Response | 0x22 | |
| Write Float | 0x23 | |
| Read Float | 0x24 | |
| Float Value Response | 0x25 | |
| Write Int | 0x26 | |
| Read Int | 0x27 | |
| Errors* | 0xE* | Different kind of error responses from the Arduino |

 **\*The different types of error messages are listed below:**
| Type: | Byte Value: | Info: |
|---|---|---|
| Error Check Sum | 0xE0 | The check sum from the message and the calculated check sum do not match |
| Error Pin ID | 0xE1 | The pin ID from the last request has no match in the Arduino script |
| Error Start Byte | 0xE2 | The first byte read from the recent message was not the specified start byte |
|...|...|...|



- Message Length Byte: Specifying how many bytes the payload containing the message is comprised of
- Check Sum: To ensure all the data that has been sent has been received correctly the check sum is calculated and sent with the message. It is calculated as: 

    $\text{Checksum} = \sum_{i=1}^{n} \mathrm{int}(b_i), \quad \text{where } b_i \text{ are all message bytes except the checksum byte itself.}$

