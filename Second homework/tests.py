import unittest
from customlist import CustomList
from metaclass import CustomMeta


class CustomListTest(unittest.TestCase):
    def test_list_methods(self):
        a = CustomList()
        count = 10
        for i in range(count):
            a.append(i)
        for i in range(count):
            self.assertEqual(a[i], i)

        a = a[::-1]
        for i in range(count):
            self.assertEqual(a[i], count - i - 1)

    def test_compare(self):
        self.assertLess(CustomList(i for i in range(10)), CustomList(i for i in range(11)))
        self.assertEqual(CustomList(i for i in range(10)), CustomList(i for i in range(9, -1, -1)))
        self.assertGreater(CustomList(i for i in range(11)), CustomList(i for i in range(10)))
        self.assertLessEqual(CustomList(i for i in range(10)), CustomList(i for i in range(11)))
        self.assertLessEqual(CustomList(i for i in range(10)), CustomList(i for i in range(10)))
        self.assertGreaterEqual(CustomList(i for i in range(11)), CustomList(i for i in range(10)))
        self.assertGreaterEqual(CustomList(i for i in range(10)), CustomList(i for i in range(10)))

    def test_addition(self):
        count1 = 10
        count2 = 5 + count1
        a1 = CustomList(i for i in range(count1))
        a2 = CustomList(i for i in range(count2))
        a3 = a1 + a2

        for i in range(count1):
            self.assertEqual(a1[i], i)
        for i in range(count2):
            self.assertEqual(a2[i], i)
        for i in range(count2):
            if i < count1:
                self.assertEqual(a3[i], i*2)
            else:
                self.assertEqual(a3[i], i)

        a11 = [i for i in range(count1)]
        a22 = [i for i in range(count2)]

        self.assertEqual(a3, a11+a2)
        self.assertEqual(a3, a1+a22)

    def test_subtraction(self):
        count1 = 10
        count2 = 5 + count1
        a1 = CustomList(i for i in range(count1))
        a2 = CustomList(i for i in range(count2))
        a3 = a1 - a2

        for i in range(count1):
            self.assertEqual(a1[i], i)
        for i in range(count2):
            self.assertEqual(a2[i], i)
        for i in range(count2):
            if i < count1:
                self.assertEqual(a3[i], 0)
            else:
                self.assertEqual(a3[i], -i)

        a11 = [i for i in range(count1)]
        a22 = [i for i in range(count2)]

        self.assertEqual(a3, a11 - a2)
        self.assertEqual(a3, a1 - a22)


class MetaclassTest(unittest.TestCase):
    def test_attributes_names(self):
        class TestClass(metaclass=CustomMeta):
            x = 0
            y = 0
            z = 0

            def get_coords(self):
                return 0, 0, 0,

        a = TestClass()
        self.assertIn('custom_x', a.__dir__())
        self.assertIn('custom_y', a.__dir__())
        self.assertIn('custom_z', a.__dir__())
        self.assertIn('custom_get_coords', a.__dir__())
        self.assertNotIn('x', a.__dir__())
        self.assertNotIn('y', a.__dir__())
        self.assertNotIn('z', a.__dir__())
        self.assertNotIn('get_coords', a.__dir__())

        self.assertEqual(a.custom_x, 0)
        self.assertEqual(a.custom_y, 0)
        self.assertEqual(a.custom_z, 0)
        self.assertEqual(a.custom_get_coords(), (0, 0, 0,))


if __name__ == '__main__':
    unittest.main()
