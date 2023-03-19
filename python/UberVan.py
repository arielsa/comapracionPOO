from car import Car

class UberVan(Car):
    typeCarAccepted=[]
    seatsMaterial = []

    def __init__(self, license, driver,seatsMaterial, typeCar):
        super().__init__(license, driver)
        self.seatsMaterial = seatsMaterial
        self.typeCarAccepted = typeCar