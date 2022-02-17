import CarClass as cc

dream_car = cc.Car(2012, "Cheverlot", "Camero")


def main():
    print("Car Year Model: ", dream_car.get_year_model())
    print("Car Make: ", dream_car.get_make())
    print("Car Model: ", dream_car.get_year_model())


for count in range(5):
    dream_car.accelerate()
    print("Speed is ", dream_car.get_speed())


for count in range(5):
    dream_car.brake()
    print("Speed is ", dream_car.get_speed())

main()
