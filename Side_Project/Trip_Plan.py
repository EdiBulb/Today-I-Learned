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

# 호텔의 방 정보 저장 딕셔너리
hotel_rooms = {
    "Single":3,
    "Double":2, 
    "Suite":1 #스위트룸 :남은 방 1개
}

# 방 예약 함수
def check_room_availability(room_type):
    if hotel_rooms.get(room_type, 0) > 0: # room_type에 해당하는 방이 존재하면 그 값을 반환한다
        print(f"Room available! A {room_type} room has been reserved for you.")
        hotel_rooms[room_type] -=1
    else:
        print(f"Sorry, no {room_type} rooms are available.")


# 숙소 예약 함수
def book_room():
    print("Available room types:")
    for room, count in hotel_rooms.items():
        print(f"{room}: {count} rooms available")
    
    room_choice = input("Which type of room would you like to book(Single/Double/Suite)?: ")

    if room_choice in hotel_rooms:
        check_room_availability(room_choice)
    else:
        print("Invalid room type. Please try again")

book_room()