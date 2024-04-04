class Square:
    """
    Class Square: defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a square

        Args:
            size (int, optional): size of the square (default is 0)
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

