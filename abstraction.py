from abc import ABC, abstractmethod

class superhero(ABC):

    @abstractmethod
    def fight_crime(self):
        pass

    @abstractmethod
    def use_power(self):
        pass

class ironman(superhero):
    def fight_crime(self):
        return "ironman is fighting crime with powerful iron suit!"
    def use_power(self):
        return "ironman uses his laser vision!"

class batman(superhero):
    def fight_crime(self):
        return "batman is fighting crime with martial arts and gadgets!"
    def use_power(self):
        return "batman uses his batmobile to chase criminals!"

ironman=ironman()
batman=batman()

print(ironman.fight_crime())
print(ironman.use_power())

print(batman.fight_crime())
print(batman.use_power())
