class Logger:
    def __init__(self):
        # Dictionary to store the latest timestamp for each message
        self.message_timestamp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # If the message is not in the dictionary or the current timestamp
        # is greater than the stored timestamp + 10, we can print the message.
        if message not in self.message_timestamp or timestamp >= self.message_timestamp[message] + 10:
            # Update the message's latest timestamp
            self.message_timestamp[message] = timestamp
            return True
        else:
            # Otherwise, we should not print the message
            return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)