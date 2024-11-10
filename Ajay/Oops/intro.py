class Item:
    def calculate_total_price(self, price , quantity):
        return price * quantity

random_str = str("Hello")
print(type(random_str))
#Every time we decalre a variable in Python we are creating an instance of 
#that particular class like <class 'str'> , <class 'int'>
random_str.upper()
#We can access the built-in functions (they are called Methos) 
#of {class str} with the instance random_str we created just now.


item1 = Item()
item1.name = "Phone"
item1.price = 200
item1.quantity = 10
tp_1 = item1.calculate_total_price(item1.price , item1.quantity)
print(type(item1))
print(f"Total price of Item1 {tp_1}")

item2 = Item()
item2.name = "Laptop"
item2.price = 800
item2.quantity = 30
tp_2 = item2.calculate_total_price(item2.price , item2.quantity)
print(f"Total price of Item2 {tp_2}")

