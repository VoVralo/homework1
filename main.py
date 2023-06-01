from datetime import datetime


class Car:

    def __init__(self, autor, mark, fuel_use, release=2020):
        self.release = release
        self.autor = autor
        self.mark = mark
        self.race = 0
        self.fuel_use = fuel_use

    def __str__(self):
        return f'Car: name: {self.mark}'

    @property
    def year(self):
        my_year = datetime.today().year - self.release
        return my_year


porshe = Car(autor='porshe ag', mark='porshe', fuel_use=11.4, release=2020)
audi = Car(autor='audi', mark='audi', fuel_use=6.8, release=2020)
nissan = Car(autor='nissan', mark='nissan', fuel_use=8.0, release=2020)
