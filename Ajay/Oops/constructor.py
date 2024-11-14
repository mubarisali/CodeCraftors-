class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all=[]
    
    #Python  passes instance itself as its first argument , so we have to pass it explicitly
    #I can pass default values for arguments like quantity = 0
    def __init__(self, name: str , price: float , quantity= 0):
        #Run validations to the received arguments
        # assert price > 0 , f"Price {price} is not greater than zero"
        assert quantity >= 0 , f"Quantity {quantity} is not greater than zero" 
        
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #actions to execute
        Item.all.append(self)
    
    #Method doesn't needs to pass the price and qunatity arguments    
    def calculate_total_price(self):
        return self.price * self.quantity
    
    def calculate_dicount(self):
        return self.price * self.pay_rate
    
    def __repr__(self):
        return f"Item('{self.name}' , {self.price} , {self.quantity})"
        
    
item1 = Item("Phone", 200 , 25)
item2 = Item("Laptop", 800 , 30)

print(item1.name)
print(item2.name)  

print(f"Total price of Item1 is {item1.calculate_total_price()}")
print(f"Total price of Item2 is {item2.calculate_total_price()}")


print(Item.pay_rate) #accessing class attributes
print(item1.pay_rate) #can access class attributes on instance levels

print(Item.__dict__) #all the attributes of class level
print(item1.__dict__) #all the attributes of instance level

item3 = Item("Tablet", 100 , 10)
item3.pay_rate = 0.5
item3_discount = item3.calculate_dicount()
print(item3_discount)

item4 = Item("Cable", 10, 5)
item5 = Item("Mouse", 50, 5)
item6 = Item("Keyboard", 75, 5)

print(Item.all)

for instance in Item.all:
    print(instance.name)