class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """

    def __init__(self):
        self._items = []

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        self._items.append(value)

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        try:
            index = self._items.index(value)
            del self._items[index]
            return True
        except ValueError:
            return False

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        # TODO: implement this method
        self._items.sort()
        size = len(self._items)
        if size == 0:
            raise Exception
        if size % 2 == 0:
            return self._items[size // 2 - 1]
        else:
            return self._items[size // 2]
