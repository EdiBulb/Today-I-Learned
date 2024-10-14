# 가고싶은 여행지 저장할 리스트
places_to_visit = []

def ask_for_places():
    print("Let's plan the trip! (Type 'end'when you're finished)")

    while True:
        place = input("Where do you want to go? (or type 'end' to finish)")
        if place.lower()=="end":
            break

        places_to_visit.append(place)
        print(f"{place} has been added to the list.\n")
    
    print("\nHere is the list of places you want to visit:")
    for i, place in enumerate(places_to_visit, 1):
        print(f"{i}. {place}")

ask_for_places()

# 사람
class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def introduction(self):
        print(f"My name is {self.name}, I'm {self.year}years old")

person1 = Person("Harry", 28)
person1.introduction()

