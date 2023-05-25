#SINGLE INHERITANCE
class rbi:
    def __init__(self):
        print("RBI:")
    def input(self):
        self.ROI=input("enter your ROI:")
class sbi(rbi):
    def display(self):
        print("Rate of interest:",self.ROI)
class hdfc(sbi):
    def display1(self):
        print("Rate of interest:",self.ROI)
obj=hdfc()
obj.input()
obj.display()
obj.display1()
print("----------------------------------")
print("HYBRID INHERITANCE")


#HYBRID INHERITANCE

class grand_child:
    def __init__(self):
        print("This is super class")
class parent1(grand_child):
    def display(self):
        print("this is parent1")
class parent2(grand_child):
    def display1(self):
        print("This is parent2")
class child(parent1,parent2):
    def dp(self):
        print("This is the only child here")
obj=child()
obj.display()
obj.display1()
obj.dp()