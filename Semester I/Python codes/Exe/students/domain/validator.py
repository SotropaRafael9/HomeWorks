class ValidatorException(Exception):
    def __init__(self, list_messages) -> None:
        self._list_messages = list_messages
    
    def get_messeges(self):
        return self._list_messages
    
    def __str__(self) -> str:
        validator_errors =  ""
        for messages in self._list_messages:
            validator_errors += messages
            validator_errors += "\n"
        return validator_errors