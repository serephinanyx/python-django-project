class pizza:
    def __init__(self,price1=10.99,price2=9.5,quantity_pizza=0,quantity_pasta=0,total="",name="",colddrink=1,bruschetta=2,chocobrwni=2):
        self.price1 = price1
        self.price2 = price2
        self.quantity_pizza=quantity_pizza
        self.quantity_pasta=quantity_pasta
        self.total=total
        self.name=name
        self.colddrink=colddrink
        self.bruschetta=bruschetta
        self.chocobrwni=chocobrwni


    def inputdetails(self):
        self.name = input("enter a customer name : ")
        print(f"Hello {self.name}, Welcome to Pizzariya")
    def food(self):
        print("""                ----------Menu--------------
              
                1 large pizza = 10.99 AUD 

                2 large Pizzas = 20.99 AUD 

                3 Large Pizzas = 29.99 AUD

                ***Buy 4 or more pizza and get 1.5lt of soft drink free***


                1 large pasta = 9.5 AUD 

                2 large pastas = 17.00 AUD 
                
                3 large pastas = 27.50 AUD

                ***Buy 4 or more pastas and get 2 bruschetta free.***
                ***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.""")
        
        status = True
        while status:
            print("""
                    1.  Pizza
                    2. Pasta
                    0. exit""")
            choice=int(input(" Order of food : "))
            if choice==1:
                self.quantity_pizza = int(input("enter a quantity "))
                if self.quantity_pizza==1:
                    self.price1=10.99
                    print(self.price1)
                    break
                elif self.quantity_pizza==2:
                    self.price1=self.price1 + 10
                    print(self.price1)
                    break
                elif self.quantity_pizza==3:
                    self.price1=self.price1+ 19
                    print(self.price1)
                    break
                elif self.quantity_pizza>=4:
                    self.price1=self.price1*self.quantity_pizza
                    print(self.price1)
                    total_quantity=self.quantity_pizza+self.colddrink
                    print(f" Quantity of pizza is {self.quantity_pizza} and \nQuantity of Soft_drink  is {self.colddrink} \nTotal quantity is : ", total_quantity)
                else:
                    print(" Invalid Quantity ")
            elif choice==2:
                self.quantity_pasta = int(input("enter a quantity "))
                if self.quantity_pasta==1:
                    self.price2=9.5
                    print(self.price2)
                    break
                elif self.quantity_pasta==2:
                    self.price2=self.quantity_pasta*9.5
                    print(self.price2)
                    break
                elif self.quantity_pasta==3:
                    self.price2=self.quantity_pasta*9.5
                    print(self.price2)
                    break
                elif self.quantity_pasta>=4:
                    self.price2=self.quantity_pasta*9.5
                    
                    print(" Total price is ",self.price2," AUD ")
                    total_quantity=self.quantity_pasta+self.colddrink
                    print(f" Quantity of pasta is {self.quantity_pasta} and \nQuantity of bruschetta is {self.bruschetta} \nTotal quantity is : ", total_quantity)
                else:
                    print(" Invalid Quantity ")
            
            elif choice==0:
                if self.quantity_pasta>=4 and self.quantity_pizza>=4:
                    total_quantity = self.quantity_pasta+self.quantity_pizza+self.chocobrwni
                    print(f" Quantity of pasta is {self.quantity_pasta},\nQuantity of pizza is {self.quantity_pizza} and \nQuantity of chocobrwni is {self.chocobrwni} Total quantity is : ", total_quantity)
                    self.price1=9.5*self.quantity_pizza
                    self.price2=self.quantity_pasta*9.5
                    print("Total amount of price is ",self.price1+self.price2)
                else:
                    pass

                # total_price = self.price1+self.price2
                # print("Total amount is : ",total_price)
                status = False
            else:
                print(" Invalid Chioce ")
            total_price = self.price1+self.price2
            print("Total amount is : ",total_price)
            print(" Bye Bye ")       
obj=pizza()
obj.inputdetails()
obj.food()


    
        

