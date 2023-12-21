class CustomException(Exception):
    def __init__(self,message):
        self.message = message

class FilesNotFound(CustomException):
    def __init__(self):
        message = "Files not found"
        CustomException.__init__(self, message)