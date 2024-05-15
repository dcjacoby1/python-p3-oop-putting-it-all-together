#!/usr/bin/env python3

class Shoe:
    #brand and size required to add object, condition optional
    def __init__(self, brand, size, condition = 'Old'):
        self.brand = brand
        self.size = size
        self.condition = condition

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    #once cobbled, changes to condition to new
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'


