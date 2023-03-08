#!/usr/bin/python3
"""Robot blueprint"""

class Robot:
    """Represents a robot, with a name"""

    #class variable
    population = 0

    def __init__(self, name):
        """Initializes the data"""
        self.name = name
        print("(Initializing {})".format(self.name))

        #When this robot is created, it adds to the population
        type(self).population += 1

    def die(self):
        """I am dying"""
        print("{} is being destroyed".format(self.name))

        type(self).population -= 1

        if type(self).population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(Robot.population))

    def say_hi(self):
        """Greetings"""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """prints curent population"""
        print("We have {:d} robots.".format(cls.population))
