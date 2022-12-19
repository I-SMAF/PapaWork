from parentClasses.DiscArray import DiscArray


class IBM(DiscArray):

    def lun_collect(self, *args):
        self.lun_create_from_data_set(data_set=args)