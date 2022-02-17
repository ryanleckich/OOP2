class retailitem:
    def __init__(self, desc, inven, price):
        self.__desc = desc
        self.__inventory = inven
        self.__price = price

    def set_desc(self, desc):
        self.__desc = desc

    def set_inventory(self, inven):
        self.__inventory = inven

    def set_desc(self, price):
        self.__price = price

    def get_desc(self):
        return self.__desc

    def get_inventory(self):
        return self.__inventory

    def get_price(self):
        return self.__price
