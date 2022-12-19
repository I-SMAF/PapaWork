"""
add every new child of DiscArray in this file
"""
from contextlib import suppress
from abc import ABC
from sys import modules
from typing import Type

from parent_classes.BaseDiscArray import BaseDiscArray

# to delete
from utils import collect, request_to_array

# every BaseDiscArray`s children (subclasses) here:
from Huawei import Huawei
from Hitachi import Hitachi
from IBM import IBM


def get_disc_array_class(*, __vendor_name: str) -> Type[BaseDiscArray]:
    """
    Method that processes string value for
    matching with valid module attribute
    and checking for is BaseDiscArray parent
    :param __vendor_name: str
    :return Type[BaseDiscArray]: children (subclasses) of BaseDiscArray
    """
    __disc_array_class = ABC
    with suppress(AttributeError):
        __disc_array_class = getattr(modules[__name__], __vendor_name)

    if issubclass(__disc_array_class, BaseDiscArray):
        return __disc_array_class
    else:
        raise Exception(f'class by {__vendor_name} vendor_name not found')


def example():
    """
    Example of generating various instances of parent class BaseDiscArray
    with the generation instances of luns of BaseLun
    """
    for disc_array in collect():
        vendor_name: str | None = disc_array.get('vendor', None)
        disc_array_class = get_disc_array_class(__vendor_name=vendor_name)(**disc_array)
        disc_array_class.lun_create_from_data_set(data_set=request_to_array())
        print(vendor_name, disc_array_class.__dict__)


example()
