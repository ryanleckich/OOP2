import CoinClass as c


def show_coin_status(coin_obj):
    print(" This side fo the coin in up", coin_obj.get_sideup())


def flip(coin_obj):
    coin_obj.toss()


my_coin = c.Coin()
show_coin_status(my_coin)

for i in range(10):

    flip(my_coin)
    show_coin_status(my_coin)
