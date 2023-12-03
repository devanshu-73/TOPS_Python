class Bird:
    def duck(self):
        self.age=3 # public
        self.__name="Donald Duck" # private
        self._sound="quack quack" # protected

class Goose(Bird):
    def display(self):
        print("This is Goose : ",self._sound)
        print("Goose name is : ",self._Bird__name)
        # Name Mangling : gain access on private data
        # Syntax : _classname__privatedata

g1=Goose()
g1.duck()
g1.display()

