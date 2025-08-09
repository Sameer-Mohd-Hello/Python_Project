class BikeStore:
    def __init__(self, stock):
        self.stock = stock

    def displayStock(self):
        print("Available bikes->", self.stock)

    def CustomerPurchase(self, Qty):
        if Qty > self.stock or Qty <= 0:
            print("Invalid quantity!")
        else:
            self.stock = self.stock - Qty
            print(Qty, "Bikes Purchased successfully")
            print("Available bikes->", self.stock)

    def restock(self, Qty):
        self.stock = self.stock + Qty
        print(Qty, "Bikes Added to stock successfully")
        print("Available bikes->", self.stock)


obj = BikeStore(100)

while True:
    choice = int(
        input(("1. Display Stock, 2. Purchase Bike, 3. Sell Bike, 4. Exit-> "))
    )
    if choice == 1:
        obj.displayStock()
    elif choice == 2:
        Qty = int(input("Enter quantity of bike to Buy->"))
        obj.CustomerPurchase(Qty)
    elif choice == 3:
        Qty = abs(int(input("Enter Qty of bike to Sell-> ")))
        obj.restock(Qty)
    else:
        break
