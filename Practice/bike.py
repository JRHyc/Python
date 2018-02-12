class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def diplay_info(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        if self.miles < 5:
          print "Stop"
        else:
          print "Reversing"
          self.miles -= 5
        
        return self

bike_1 = Bike(100, "25 mph")
bike_2 = Bike(150, "30 mph")
bike_3 = Bike(200, "35 mph")

bike_1.ride().ride().ride().reverse().diplay_info()
bike_2.ride().ride().reverse().reverse().diplay_info()
bike_3.reverse().reverse().reverse().diplay_info()
