product=[]
qty_list=[]
price=[]
data="""
                        WELCOME TO JAY BHAVANI
                        
                                 MENU
                ------------------------------------------    
                    PRODUCT               PRICE
                -------------------------------------------    
                    
                    VADAPAV                  30

                    DABELI                   30

                    BHEL                     70


                    """
print(data)

for i in range(1,3):
    product_name=input("enter your product:").upper()
    qty=int(input("enter number of quantity you want :"))
    if product_name=="VADAPAV" or product_name=="DABELI":
        price_value=30
        totale_price=price_value*qty

        product.append(product_name)
        qty_list.append(qty)
        price.append(totale_price)
    
    
    elif product_name=="BHEL":
         price_value=70
         totale_price=price_value*qty

         product.append(product_name)
         qty_list.append(qty)
         price.append(totale_price)
        
         for i in range (0,len(product)):
          print(f"{product[i]}  {qty_list[i]}={price[i]}")
    else:
        print("invalid input")


for i in range(0,len(product)):
    print(f"{product[i]}  {qty_list[i]}={price[i]}")

print("--------------REMOVE PRODUCT---------------")
product_name=input("enter product which you want to remove:").upper()
position= product.index(product_name)
product.pop(position)
qty_list.pop(position)
price.pop(position)

for i in range (0,len(product)):
    print(f"{product[i]}  {qty_list[i]}={price[i]}")



