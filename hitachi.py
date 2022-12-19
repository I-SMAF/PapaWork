"""
Hitachi class of BaseDiscArray
"""
from parent_classes.base_disc_array import BaseDiscArray


class Hitachi(BaseDiscArray):
    """
    class with override __init__ & lun_collect (example)
    """

    def __init__(
            self,
            *,
            instance_id: int,
            proxy: int,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.instance_id = instance_id
        self.proxy = proxy

    def lun_collect(
            self,
            *args
    ):
        self.lun_create_from_data_set(data_set=args)
