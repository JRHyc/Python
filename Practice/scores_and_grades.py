import random
random_num = int(random.randint(60,100))


def grades():
    for j in range(0,10):
        num = int(random.randint(60,100))
        if(num >= 90 and num <= 100):
            print "Score {}. Your grade is an A".format(num)
        elif(num >= 80 and num < 90):
            print "Score {}. Your grade is an B".format(num)
        elif(num >= 70 and num < 80):
            print "Score {}. Your grade is an C".format(num)
        elif(num >= 60 and num < 70):
            print "Score {}. Your grade is an D".format(num)

grades()


