from application import say_hello
import unittest


def test_say_hello():
    name = "Ahmet"
    real_value = say_hello(name=name)
    assert real_value == {"message": f"Hello {name}"}


if __name__ == "__main__":
    unittest.main()
