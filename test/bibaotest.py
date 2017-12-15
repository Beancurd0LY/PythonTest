# coding=utf-8
def plus(number):
    def plus_in(number_in):
        print str(number_in) + "number_in"
        return number+number_in
    return plus_in


v1=plus(20)
print v1(100)
