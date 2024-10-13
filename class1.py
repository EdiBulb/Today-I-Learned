class Car:
    # 생성자
    def __init__(self, brand, model, year):
        # 속성 정의
        self.brand = brand
        self.model = model
        self.year = year
    
    # 메서드 정의
    def start_engine(self):
        print(f"{self.brand} {self.model}'s engine has started!")
    

my_car = Car("Toyota","Corolla", 2020)
my_car.start_engine()

# 상속
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
    
    def charge_battery(self):
        print(f"The battery of {self.brand} {self.model} is charging")

    # 메서드 오버라이딩
    def start_engine(self):
        print(f"{self.brand} {self.model} is starting silently because it's electric!")
    
my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

my_electric_car.start_engine() # 부모 클래스 메서드 사용
my_electric_car.charge_battery() # 자식 클래스 메서드 사용
    

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
my_electric_car.start_engine()
