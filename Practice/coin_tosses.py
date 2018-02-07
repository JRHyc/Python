x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1

import random
random_num = random.random()
print random_num
outcome = round(random_num)
print outcome

def coin_toss(num):
    random_num = random.random()
    outcome = round(random_num)
    for i in range(0, 5000):
        if outcome == 1:
            print "Its heads!"
        else:
            print "Its tails!"

coin_toss()
