import time

from cookiecutter_pyapp_test.core import hello_world


def run():
    while True:
        print(hello_world())
        time.sleep(1)
