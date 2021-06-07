import unittest
import rev


class TestClass(unittest.TestCase):
    def test_rev_1(self):
        self.assertEqual(rev.rev("This is a test"), "test a is This")

    def test_rev_2(self):
        self.assertEqual(rev.rev("My name is Ryan Zimmerman"),
                         "Zimmerman Ryan is name My")


class TestReverseApp:
    def test_1(self):
        assert rev.rev("This is not a drill") == "drill a not is This"

    def test_2(self):
        assert rev.rev("This is a test of the emergency broadcast system"
                       ) == "system broadcast emergency the of test a is This"


if __name__ == '__main__':
    unittest.main()