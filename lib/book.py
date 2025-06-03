# -*- coding: utf-8 -*-

from __future__ import print_function  # ✅ Enables Python 3 style print in Python 2
from __future__ import unicode_literals

class Book(object):  # ✅ Explicit inheritance for Python 2 compatibility
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count  # uses setter

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
