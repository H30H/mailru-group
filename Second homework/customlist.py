class CustomList(list):
    def __add__(self, other):
        if not isinstance(other, list):
            raise TypeError('Obj not a list')

        if len(self) > len(other):
            res = CustomList(self)
            for i in range(len(other)):
                res[i] += other[i]
            return res
        else:
            res = CustomList(other)
            for i in range(len(self)):
                res[i] += self[i]
            return res

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if not isinstance(other, list):
            raise TypeError('Obj not a list')

        invert_other = [-i for i in other]
        return self.__add__(invert_other)

    def __rsub__(self, other):
        return CustomList(other).__sub__(self)

    def __lt__(self, other):
        if not isinstance(other, list):
            raise TypeError('Obj not a list')

        return sum(self) < sum(other)

    def __eq__(self, other):
        if not isinstance(other, list):
            raise TypeError('Obj not a list')

        return sum(self) == sum(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = CustomList([5, 4, 3, 2, 1])
    print(list1, list2)
    print(list1 + list2, list2 + list1)
    print(list1 - list2, list2 - list1)