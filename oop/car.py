class Car(object):
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        # print(f"{self.manufacturer}の{self.model_name}(燃費：{self.mileage}) 、アクセル全開！")
        print("{0.manufacturer}の{0.model_name}(燃費：{0.mileage}) 、アクセル全開！".format(self))

    def brake(self):
        print(f"{self.model_name} is stopping")






if __name__ == "__main__":
    prius = Car("Prius", 20, "Toyota")
    prius.gas()
    prius.brake()