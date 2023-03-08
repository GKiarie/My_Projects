#!/usr/bin/python3
"""A person class"""

class Person:
    """Person class"""
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)
