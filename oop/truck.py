from car import Car

class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_loadings):
        super().__init__(model_name, mileage, manufacturer)
        self._max_loading = max_loadings
        self._loadings = 0
    
    def gas(self):
        if self._loadings > self._max_loading:
            print(f"最大積載量{self._max_loading}kgを超えています！発進できません！！")
        else:
            super().gas()

    def load(self, weight):
        if weight > 0:
            self._loadings += weight
            print(f"荷物を{weight}kg積みました")
        else:
            #荷物を下ろす
            if self._loadings <= -weight:
                self._loadings = 0
                print("荷物を降ろしました")
            else:
                self._loadings += weight
                print(f"荷物を{-weight}kg下ろしました")
        
        if self._loadings > self._max_loading:
            print(f"最大積載量{self._max_loading}kgを超えています！")

if __name__ == "__main__":
    isuzu = Truck("トラックA", 10, "Isuzu", 1000)
    isuzu.gas()
    isuzu.load(100)
    isuzu.gas()