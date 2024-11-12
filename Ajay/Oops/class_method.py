import csv

class Item:
    all = []  # Class-level attribute to store all instances

    def __init__(self, name: str, price: float, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)  # Add each new instance to the class-level list

    def calculate_total_price(self):
        return self.price * self.quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open('C:\\Users\\User\\Desktop\\MufilRahman\\CodeCraftors-\\Ajay\\Oops\\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )
            
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
         

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


# Instantiate items from CSV
Item.instantiate_from_csv()

# Print all instantiated items
print(Item.all)
