"""
add every new child of DiscArray in this file
"""
import contextlib
from abc import ABC
from sys import modules
from parentClasses.DiscArray import DiscArray

# to delete
from utils import collect, request_to_array

# every DiscArray`s children (subclasses) here:
from Huawei import Huawei
from Hitachi import Hitachi
from IBM import IBM


def get_disc_array_class(*, __vendor_name):
    __disc_array_class = ABC
    with contextlib.suppress(AttributeError):
        __disc_array_class = getattr(modules[__name__], __vendor_name)

    if issubclass(__disc_array_class, DiscArray):
        return __disc_array_class
    else:
        raise Exception(f'class by {__vendor_name} vendor_name not found')


for disc_array in collect():
    vendor_name: str | None = disc_array.get('vendor', None)
    disc_array_class = get_disc_array_class(__vendor_name=vendor_name)(**disc_array)
    disc_array_class.lun_create_from_data_set(data_set=request_to_array())
    print(vendor_name, disc_array_class.__dict__)
