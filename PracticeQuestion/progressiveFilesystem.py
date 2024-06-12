from abc import ABC


class IntegerContainer(ABC):
    """
    `IntegerContainer` interface.
    """

    def add(self, value: int) -> int:
        """
        Should add the specified integer `value` to the container
        and return the number of integers in the container after the
        addition.
        """
        # default implementation
        return 0

    def delete(self, value: int) -> bool:
        """
        Should attempt to remove the specified integer `value` from
        the container.
        If the `value` is present in the container, remove it and
        return `True`, otherwise, return `False`.
        """
        # default implementation
        return False

    def get_median(self) -> int | None:
        """
        Should return the median integer - the integer in the middle
        of the sequence after all integers stored in the container
        are sorted in ascending order.
        If the length of the sequence is even, the leftmost integer
        from the two middle integers should be returned.
        If the container is empty, this method should return `None`.
        """
        # default implementation
        return None


from integer_container import IntegerContainer


class IntegerContainerImpl(IntegerContainer):

    def __init__(self):
        # TODO: implement
        self._items = []

    # TODO: implement interface methods here
    def add(self, value: int) -> int:
        self._items.append(value)
        return len(self._items)

    def delete(self, value: int) -> bool:
        try:
            index = self._items.index(value)
            del self._items[index]
            return True
        except:
            return False

    def get_median(self) -> int | None:
        if len(self._items) == 0:
            return None
        self._items.sort()
        mid = len(self._items) // 2
        if len(self._items) % 2 == 0:
            mid -= 1
        return self._items[mid]
