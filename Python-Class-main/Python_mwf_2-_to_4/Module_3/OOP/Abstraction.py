'''
    Abstraction : "Hidding irrelevant data from the user"

    in we can achive abstraction using ABC(Abstract Base Class)

'''

from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def roi(self):
        print("SBI take 5% interest on Home Loan")

class HDFC(RBI):
    def roi(self):
        print("HDFC take 5% interest on Home Loan")


s1=SBI()
s1.roi()

h1=HDFC()
h1.roi()



        
