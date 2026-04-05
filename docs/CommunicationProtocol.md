# Communication Protocol

To communicate with the Arduino's pins we have a script running on the Arduino that continuously waits for a request from the main script on the computer. The communication medium are sequences of bytes that have a very specific structure:

```
[Start Sequence Byte] -> [Message Type Byte] -> [Message Length Byte] -> [...][Payload][...] -> [Check Sum Byte]
```

- Start Sequence Byte: Byte containing the start sequence signaling the start of a message.
- Message Type Byte: Type of message. The message can be one of the following types:

| Message Type: | Info: |
|---|---|
| Write Digital | Sending a write request for a digital pin to the Arduino and awaiting a Confirmation response |
| Read Digital | Sending a reading request for the value of a digital pin to the Arduino and awaiting the value response| 
| Digital Value Response | |
| Write Analogue | |
| Read Analogue | |
| Analogue Value Response
| Writing Confirmation | |
| Write Reset | | 
| Write String | |
| Read String | |
| String Value Response | |
| Write Float | |
| Read Float | |
| Float Value Response | |
| Write Int | |
| Read Int | |
| Errors* | |

 **\*The different types of error messages are listed below:**
| Type: | Info: |
|---|---|
| Error Check Sum | |
| Error Pin ID | |
| Error Start Byte | |



Message Length Byte:
Check Sum:
