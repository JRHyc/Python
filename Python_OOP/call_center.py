class Call(object):
    def __init__(self, id_number, name, phone, time, reason):
        self.id_number = id_number
        self.name = name
        self.phone = phone
        self.time = time
        self.reason = reason

    def display_all(self):
        print self.id_number
        print self.name
        print self.phone
        print self.time
        print self.reason

class Call_center(object):
    def __init__(self, calls):
        self.calls = calls
        self.list = []
        self.queue = 0

    def add_call(self, new_call):
        self.new_call = new_call
        self.list.append(self.new_call)
        self.queue = len(self.list)
        print self.queue
        print self.list
        return self

    # def remove_call(self):
    #     self.list.pop(0)
    #     self.queue = len(self.list)
    #     print self.queue
    #     print self.list
    #     return self

hospital = Call_center(0)

call1=Call(27,"Kelly","640-298-2999","5:05 A.M.","Murder")
call2=Call(45,"Joseph","757-858-8888","1:30 P.M.","I also murdered someone")
call3=Call(87,"Dan","848-848-3939","4:30 P.M","I'm being murdered!!!")
call4=Call(88,"Joseph","757-858-8888","5:02 P.M","I am murdering again.")

# call1.display_all()
# call2.display_all()
# call3.display_all()
# call4.display_all()

hospital.add_call(call1).add_call(call2).add_call(call3).remove_call().remove_call().add_call(call4).remove_call()
