from parent_classes.BaseDiscArray import BaseDiscArray


class Huawei(BaseDiscArray):

    def lun_collect(self, *args):
        self.lun_create_from_data_set(data_set=args)
