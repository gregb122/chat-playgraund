class BaseException(Exception):
    pass

class InputException(BaseException):
    pass

class AdminUserameException(InputException):
    def __init__(self):
        self.name = f'Username must not contain the world admin!'
        