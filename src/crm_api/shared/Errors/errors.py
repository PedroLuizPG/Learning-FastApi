class AppError(Exception):
    def __init__(self, message:str, statusCode: int = 400):
        self.message = message
        self.statusCode = statusCode
        super().__init__(message)