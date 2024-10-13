class Car:
    # 생성자
    def __init__(self, brand, model, year):
        # 속성 정의
        self.brand = brand
        self.model = model
        self.year = year
    
    # 메서드 정의
    def start_engine(self):
        print("f{self.brand} {self.model}'s engine has started!")
    

my_car = Car("Toyota","Corolla", 2020 )
my_car.start_engine()