import CellPhoneClass as c

iphone = c.CellPhone("Apple", "Iphone 13", "2021")


def main():

    print(iphone.get_manufact(), " : is your manufacter")
    print(iphone.get_model(), " : is your model type")
    print(iphone.get_retail_price(), " : is your retail price")


main()
