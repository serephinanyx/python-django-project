
role="""
    SELECT YOUR ROLE:
        PRESS 1 FOR DOCTOR
        PRESS 2 FOR PATIENT
    """
print(role)
    
choice=int(input("enter your role:"))
if choice==1:
    
    class User:
       def __init__(self):
        print("user class")
       def input(self):
        self.email=input("enter your email:")
        self.password=input("enter password:")
    class Doctor(User):
         def doc_input(self):
          self.specification=input("enter specification:")
         def display(self):
           print("doctor email:",self.email)
           print("doctor password:",self.password)
           print("doctor specification:",self.specification)
    obj=Doctor()
    obj.input()
    obj.doc_input()
    obj.display()

    
elif choice==2:
    class User:
       def __init__(self):
        print("user class")
       def input(self):
        self.email=input("enter your email:")
        self.password=input("enter password:")
    class Patient(User):
      def pat_input(self):
        self.blood_group=input("enter your blood group:")
      def dp(self):
        print("patient email:",self.email)
        print("patient password:",self.password)
        print("patient specification:",self.blood_group)
    obj1=Patient()
    obj1.input()
    obj1.pat_input()
    obj1.dp()