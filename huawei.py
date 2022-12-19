"""
Huawei class of BaseDiscArray
"""
from parent_classes.base_disc_array import BaseDiscArray


class Huawei(BaseDiscArray):
    """
    class with override lun_collect (example)
    """

    def lun_collect(
            self,
            *args
    ):
        self.lun_create_from_data_set(data_set=args)
