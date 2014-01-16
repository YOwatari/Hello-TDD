#!/user/bin python
# -*- coding: utf-8 -*-

def pytest_generate_tests(metafunc):
    """
    Parametrizing test methods through per-class configuration
    http://pytest.org/latest-ja/example/parametrize.html#id5
    """
    try:
        funcarglist = metafunc.cls.params[metafunc.function.__name__]
    except AttributeError:
        return
    argnames = list(funcarglist[0])
    metafunc.parametrize(
        argnames,
        [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    )

class TestFizzBuzz:
    def test_says_one(self):
        from FizzBuzz import *
        fb = FizzBuzz(1)
        assert fb.says() == "1"

    def test_says_fizz(self):
        from FizzBuzz import *
        fb = FizzBuzz(3)
        assert fb.says() == "Fizz"

    def test_says_buzz(self):
        from FizzBuzz import *
        fb = FizzBuzz(5)
        assert fb.says() == "Buzz"

    def test_says_fizzbuzz(self):
        from FizzBuzz import *
        fb = FizzBuzz(15)
        assert fb.says() == "FizzBuzz"