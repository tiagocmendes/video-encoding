
class JPEG1:
    """
    JPEG1 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return a

class JPEG2:
    """
    JPEG2 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return b

class JPEG3:
    """
    JPEG3 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return c

class JPEG4:
    """
    JPEG4 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return int(a) + int(b) - int(c)

class JPEG5:
    """
    JPEG5 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return int(a) + ((int(b) - int(c)) // 2)  # TODO: ver se tem de ser inteiro

class JPEG6():
    """
    JPEG6 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return int(b) + ((int(a) - int(c)) // 2)

class JPEG7:
    """
    JPEG7 linear predictor.
    """
    @staticmethod
    def predict(a, b, c):
        return (int(a) + int(b)) // 2

class JPEGLS:
    """
    JPEG-LS predictor
    """
    @staticmethod
    def predict(a, b, c):
        if c >= max([a, b]):
            return min([a, b])
        elif c <= min([a, b]):
            return max([a, b])
        return int(a) + int(b) - int(c)