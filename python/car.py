from acount import Acount

class Car:
    id      =int
    license =str
    driver  =Acount("","")
    passenger= int

    def __init__(self,license,driver):
        self.license=license
        self.driver=driver