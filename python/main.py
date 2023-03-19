from car import Car
from acount import Acount



if __name__=="__main__":
    print("hola mundo")

    auto1=Car()
    auto1.license="abc 123"
    auto1.id=123456
    auto1.driver="juan perez"
    auto1.passenger="pepe gomez"
    print(vars(auto1))

    auto2=Car()
    auto2.license="fjg 456"
    auto2.id=456789
    auto2.driver="matias gimenez"
    auto2.passenger="tomas sanchez"
    print(vars(auto2))
    



