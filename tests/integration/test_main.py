import sys

sys.path.insert(0, "../../application.py")
from application import say_hello


def test_say_hello():
    name = "Ahmet"
    real_value = say_hello(name=name)
    assert real_value == {"message": f"Hello {name}"}
