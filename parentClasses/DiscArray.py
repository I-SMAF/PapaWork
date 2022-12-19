from typing import Iterable, Type
from abc import ABC, abstractmethod
from types import TracebackType

from parentClasses.Lun import Lun


class DiscArray(ABC):

    def __init__(self, name: str, vendor: str):
        """
        :param name: str
        :param vendor: str
        """
        self.lun_set: set = set()
        self.name = name
        self.lun_collect()

    @staticmethod
    def lun_create_from_data(
            **kwargs
    ) -> Lun:
        """
        :param kwargs:
        **{
            -:param name: str
            -:param uid: str
            -:param size: int
        }
        :return:
        """
        lun = Lun(**kwargs)
        return lun

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
        __lun_set: set = set(
            self.lun_create_from_data(**__lun) for __lun in data_set
        )
        self.lun_set = __lun_set
        return self.lun_set

    @abstractmethod
    def lun_collect(
            self
    ):
        # to representation with
        pass

    def __enter__(
            self
    ):
        """
        :return None:
        """
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
