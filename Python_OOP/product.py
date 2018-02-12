
class Product(object):
    def __init__(self, price, item_name, weight, brand, status = "for sale", tax = 0, ret_reason = ""):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.tax = tax
        self.ret_reason = ret_reason
        self.display_all()
        
    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self, tax):
        self.tax = tax
        final_price = (self.price * self.tax) + self.price
        self.price = final_price
        return self

    def ret(self, ret_reason):
        self.ret_reason = ret_reason
        if self.ret_reason == "defective":
            self.status = "defective"
            self.price = 0
        elif self.ret_reason == "like new":
            self.status = "for sale"
        elif self.ret_reason == "used":
            self.status = "used"
            self.price = self.price * .8
        return self

    def display_all(self):
        print self.price
        print self.item_name
        print self.weight
        print self.brand
        print self.status
        print self.tax
        print self.ret_reason
        return self

product_1 = Product(2000, "couch", "150 lbs", "Lazy Boy")
prodcut_2 = Product(1000, "table", "50 lbs", "Ashley")

product_1.sell()
product_1.add_tax(.1)
# product_1.ret("like new")
# product_1.ret("defective")
product_1.ret("used")

product_1.display_all()
        