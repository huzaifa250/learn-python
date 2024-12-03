import unittest


def func(n1):
    val = n1
    if n1 > 0:
        return val
    return None


class TestFunc(unittest.TestCase):
    def test_func(self):
        self.assertEqual(func(10), 10)  # it should return True cause 10 > 1
        assert func(10) == 42.  # error


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())  # True
        self.assertFalse('Foo'.isupper())  # False

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            # verify that a specific exception gets raised
            s.split(2)  # will pass casue it's expected typeError


if __name__ == '__main__':
    unittest.main()
