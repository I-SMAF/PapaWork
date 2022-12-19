from parentClasses.BaseDiscArray import BaseDiscArray


class Hitachi(BaseDiscArray):
    def __init__(self, *, instance_id: int, proxy: int, **kwargs):
        super().__init__(**kwargs)
        self.instance_id = instance_id
        self.proxy = proxy

    def lun_collect(self, *args):
        self.lun_create_from_data_set(data_set=args)
