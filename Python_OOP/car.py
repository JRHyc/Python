class Car(object):
    def __init__(self, price, speed, fuel, mileage, tax = .12):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = tax
        if self.price > 10000:
            self.tax = .15
        self.display_all()

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self

ford = Car(5000, "80 mph", "Almost full", "25 mpg")
chevy = Car(3000, "70 mph", "Almost empty", "20 mpg")
bmw = Car(28000, "90 mph", "Empty", "28 mpg")
audi = Car(19000, "100 mph", "Almost Empty", "30 mpg")
honda = Car(16000, "65 mph", "Half full", "40 mpg")
toyota = Car(35500, "50 mph", "Half empty", "44 mpg")

