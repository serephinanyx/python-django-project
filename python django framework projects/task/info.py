name=input("Please Enter First Name:")
if name=="":
      print("You didn't enter any character.")
elif len(name.title())==1:
    print("There is ",len(name),"letters in" ,name.title())
elif name.isalpha():
    for index,letter in enumerate(name.title(),1):
        print(index,":",letter)
    print("There are ",len(name),"letters in" ,name.title())
elif name.isalnum():
    print("Non Alphabetic characters were entered.")
else:
    f=filter(str.isalpha,name)
    s1="".join(f)
    print(s1)
    for index,letter in enumerate(name.title(),1):
        print(index,":",letter)
    print("There are ",len(s1),"letters in" ,name.title())