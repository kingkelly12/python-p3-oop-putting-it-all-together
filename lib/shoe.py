# -*- coding: utf-8 -*-

from __future__ import print_function  # ✅ For Python 3 style printing
from __future__ import unicode_literals


class Shoe(object):  # ✅ Explicit inheritance
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = None  # ✅ Initialize condition to prevent attribute error

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
