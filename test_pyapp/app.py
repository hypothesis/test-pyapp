import time

from test_pyapp.core import hello_world


def run():
    while True:
        print(hello_world())
        time.sleep(1)
