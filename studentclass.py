from doctest import DONT_ACCEPT_BLANKLINE
from unicodedata import name

from matplotlib.transforms import BboxBase
from datetime import date


class Student:
    def __int__(self, studentID, name, DOB, classification):
        self.studentID = studentID
        self.name = name
        self.dob = DOB
        self.classification = classification

    def set_reg_time(self, classification):
        if classification == "Sr":
            self.__reg_time = "Registration date: 11/1 thru 11/3"
        elif classification == "Jr":
            self.__reg_time = "Registration date: 11/4 thru 11/6"
        elif classification == "S":
            self.__reg_time = "Registration date: 11/7 thru 11/9"
        else:
            self.__reg_time = "Registration date: 11/10 thru 11/12"

    def set_age(self, DOB):
        today = date.today()
        self.__age = today.year - self.__dob

    def get_age(self):
        return self.__age

    def get_reg_time(self):
        return self.__reg_time
