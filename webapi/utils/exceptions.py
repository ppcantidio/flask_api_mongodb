class ValidationError(Exception):
    def __init__(self, message):
        self.message  = message


class SecurityError(Exception):
    pass