"""
module for Generic classes of Lun
"""
from typing import Type
from types import TracebackType


class BaseLun:
    """
    Basic class describing a mandatory basics of
    methodologies and attributes of all subsequent
    classes to work with server disk arrays
    """

    def __init__(self, *, name: str, uid: str, size: int):
        """
        :param name: str
        :param uid: str
        :param size: int
        """
        self.name = name
        self.uid = uid
        self.size = size

    def __enter__(
            self
    ):
        return self

    def __exit__(
            self,
            _type: Type[BaseException] | None,
            _value: BaseException | None,
            traceback: TracebackType | None
    ) -> bool:
        """
        :param _type: Type[BaseException] | None
        :param _value: BaseException | None
        :param traceback: TracebackType | None
        :return True: bool
        """
        return True
