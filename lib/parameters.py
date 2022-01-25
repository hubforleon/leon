from re import I


def addmore(*numbers):
    sum = 0
    print("the numbers to be added are",numbers)
    for item in numbers:
        sum += item
    return sum

def showmore(**students):
    print("---- show dict input-------")
    for k, v in students.items():
        print("key: {}, value: {}".format(k,v))

# showmore(wname = "tony",wage=18)

