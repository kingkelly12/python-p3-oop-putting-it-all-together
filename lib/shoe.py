#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color):
        self.brand = brand
        self.size = size
        self.color = color
        
        print(f"Shoe '{self.brand}' of size {self.size} and color {self.color}")
        
    def __repr__(self):
        return f"Shoe({self.brand!r}, {self.size!r}, {self.color!r})"
        
    def __str__(self):
        return f"{self.brand} shoe of size {self.size} in {self.color} color"
    