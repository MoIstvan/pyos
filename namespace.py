import sys
class Name():
    def delete(fileArg:str):
        if sys.version_info >= (3, 4):
            from pathlib import Path
            Path.unlink(fileArg)

        if sys.version_info <= (3, 3):
            print("Python 3.4 or newer required")
            pass

    if sys.version_info >= (3, 4):
        class CrashError(BaseException):
            "Throws this error instead of the system crashing."
            ...
        class NotFoundError(BaseException):
            "Throws this error if something is missing."
            ...
        class ExtError(BaseException):
            "Throws this error if an extension of an application is corrupted."
            ...
        class UnknownError(BaseException):
            "Throws this error if the system doesn't knows how or where are things off."
            ...