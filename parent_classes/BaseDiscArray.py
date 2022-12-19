from typing import Iterable, Type
from abc import ABC, abstractmethod
from types import TracebackType

from parent_classes.BaseLun import BaseLun

_BASE_LUN_CLASS = BaseLun


class BaseDiscArray(ABC):
    """
    Basic abstract class describing a mandatory
    basics of methodologies and attributes of all
    subsequent classes to work with server disk arrays
    """

    def __init__(self, name: str, vendor: str):
        """
        :param name: str
        :param vendor: str
        """
        self.lun_set: set = set()
        self.name = name

    @staticmethod
    def lun_create_from_data(
            __lun_class: Type[_BASE_LUN_CLASS] = _BASE_LUN_CLASS,
            **kwargs
    ) -> BaseLun:
        """
        method for generate Lun instance
        :param __lun_class: Type[BaseLun]
        :param kwargs:
        **{
            -:param name: str
            -:param uid: str
            -:param size: int
        }
        :return Lun:
        """
        return __lun_class(**kwargs)

    def lun_create_from_data_set(
            self,
            *,
            data_set: Iterable
    ) -> set:
        """
        :param data_set: typing.Iterable
        [
            **{
                -:param name: str
                -:param uid: str
                -:param size: int
            }
        ]
        :return self.lun_set: set
        """
        self.lun_set = set(
            self.lun_create_from_data(**__lun) for __lun in data_set
        )
        return self.lun_set

    @abstractmethod
    def lun_collect(  # to representation with override
            self
    ):
        pass

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
