class CustomMeta(type):
    def __new__(cls, class_name, class_bases, class_dct):
        attributes = dict((name, value,) if name[:2] == '__' and name[-2:] == '__' and len(name) > 4 else ('custom_'+name, value,) for name, value in class_dct.items())
        return type.__new__(cls, class_name, class_bases, attributes)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


if __name__ == '__main__':
    inst = CustomClass()
    inst.abcde = 4
    print(inst.__dir__())
    print(inst.abcde)
    # inst.custom_x
    # inst.custom_val
    # inst.custom_line()

    # inst.x  # ошибка
    # inst.val  # ошибка
    # inst.line() # ошибка
