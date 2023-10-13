class Student:
    """This class creates a student object"""
    #constructor
    def __init__(self, first, last, reg_no):
        #instance variables
        self.first=first
        self.last=last
        self.reg_no=reg_no
    @property
    def email(self):
        #calc_age take birthyear and returns a new object
        return "{}.{}@email.com".format(self.first, self.last)
    
    @property
    def fullname(self):
        #calc_age take birthyear and returns a new object
        return "{} {}".format(self.first, self.last)
    
    def __repr__(self):
        return "student('{}','{}','{}')".format(self.first, self.last, self.reg_no)
