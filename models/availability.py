class Availability():
    def __init__(self, time_slot, available, booked_by):
        if type(time_slot) != str:
            raise TypeError
            
        if available == "Yes" or available == "No":
            self.available = available
        else:
            raise ValueError
    
        self.time_slot = time_slot
        self.booked_by = booked_by

    def to_dict(self):
        availability_as_dict = {}
        availability_as_dict["time_slot"] = self.time_slot
        availability_as_dict["available"] = self.available
        availability_as_dict["booked_by"] = self.booked_by
        return availability_as_dict

