from application import say_hello
import unittest


class TestApi(unittest.TestCase):
    def test_say_hello(self):
        name = "Ahmet"
        real_value = say_hello(name=name)
        assert real_value == {"message": f"Hello {name}"}


if __name__ == "__main__":
    unittest.main()
