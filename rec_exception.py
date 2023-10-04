class MyError(Exception):
    """Exception class with some value"""

    def __init__(self):
        self.values = []


    def __add__(self, val):
        self.values.append(val)
        return self


def getMyError(n: int or str) -> None:
    """Raise recursive error"""
    
    try:
        if ord(n) <= ord("A"):
            raise MyError
        getMyError(chr(ord(n) - 1))

    except MyError as error:
        raise error + n


def getList(n: int or str) -> list:
    try:
        getMyError(n)

    except MyError as error:
        return error.values


A = getList("D")
print(A)
B = getList("P")
print(B)
