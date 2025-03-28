class Human:

    def __init__(self, name='Human'):
        self.name = name

class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *args):
        for p in args:
            self.passengers.append(p)

    def print_passengers_names(self):
        if self.passengers:
        print(f'Names of {self.brand} passengers:')
        for passenger in self.passengers:
            print(passenger.name)
        else:
            print(f'There are no passengers in {self.brand}')

nick = Human ('Nick')
kate = Human ('Kate')
car = Auto('Mercedes')
car.add_passenger (nick, kate)
car.print_passengers_names()

import random

class Human:

    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home (self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self):
        pass

    def is_alive(self):
        pass

    def live(self):
        pass

