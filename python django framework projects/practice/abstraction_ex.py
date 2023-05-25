# in inheritance , child class can access all the properties of parent class that mean there is a lack of security.
# to provide more security , we can use abstraction class.
#ABSTRACTION: it shows only informations and hide core functionality.
# to achieve abstraction concept, we need to use abstract class.
#to achieve we need to import ABC
#ABC: stands for Abstract Base Class


"""
abstractmethod : which contains only method declaration - no body.

this kind of method doesn't contain method definition.

"""

from abc import ABC,abstractmethod

class RBI(ABC):
    @abstractmethod
    def roi(self):
        pass   #method declaration only
class SBI(RBI):
    def roi(self):
        print("6.5")
class HDFC(RBI):
    def roi(self):
        print("7.5")
sbi=SBI()
hdfc=HDFC()
sbi.roi()
hdfc.roi()
                