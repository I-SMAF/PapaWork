from parentClasses.BaseDiscArray import BaseDiscArray


class IBM(BaseDiscArray):

    def lun_collect(self, *args):
        self.lun_create_from_data_set(data_set=args)
