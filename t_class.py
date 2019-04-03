#encoding:UTF-8
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print '%s: %s' % (self.name, self.score)
    def a_t(self,a):
        print "This is a:"+str(a)
    def b_t(self,b,a):
        self.a_t(a)
        print "This is b:"+str(b)
Stu = Student(11,12)
Stu.b_t(5,10)