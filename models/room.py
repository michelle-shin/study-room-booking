class Room():
    def __init__(self, number):
        self.number = number
        self.availability = []

    def add_availability(self, availability):
        self.availability.append(availability.to_dict())
      
    def get_room_bookings(self):
        room_booking = {}
        room_booking["room_number"] = self.number
        room_booking["availability"] = self.availability
        return room_booking


    # def details(self):
    #     print(self.number)
    #     for availability in self.availability:
    #         print(availability["time_slot"])
    #         print(availability["available"])
    #         print(availability["booked_by"])
