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

    #returns availibility of a room of given timeslot
    def get_availibility(self, time_slot):
        for availibiity in self.availability:
            if availibiity["time_slot"]==time_slot:
                return availibiity

    def book(self, id, time_slot):
        for availability in self.availability:
            if availability["time_slot"]==time_slot:
                availability["available"] = "No"
                availability["booked_by"] = id
    
    def cancel_booking(self, id, time_slot):
        for availability in self.availability:
            if availability["time_slot"]==time_slot and availability["booked_by"]==id:
                availability["available"] = "Yes"
                availability["booked_by"] = ""

