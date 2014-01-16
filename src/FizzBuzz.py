#!/user/bin python
# -*- coding: utf-8 -*-

class FizzBuzz(object):
    def __init__(self, number):
        self.__current = number

    def says(self):
        if self.__current % 3 == 0 and self.__current % 5 == 0:
            return "FizzBuzz"
        elif self.__current % 3 == 0:
            return "Fizz"
        elif self.__current % 5 == 0:
            return "Buzz"
        else:
            return str(self.__current)

