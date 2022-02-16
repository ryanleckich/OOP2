from pyexpat import model
from sys import maxunicode


class CellPhone:
    def __int__(self, manu, model, retail):
        self.__manufact = manu
        self.__model = model
        self.__retail_price = retail

    def set_maunfact(self, manu):
        self.__manufact = manu

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail):
        self.__retail_price = retail

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
