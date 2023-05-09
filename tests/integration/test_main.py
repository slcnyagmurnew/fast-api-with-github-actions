import sys,os
from pathlib import Path
path = Path(os.getcwd())
sys.path.append(str(path.parent))

from application import say_hello


def test_say_hello():
    name = "Ahmet"
    real_value = say_hello(name=name)
    assert real_value == {"message": f"Hello {name}"}
