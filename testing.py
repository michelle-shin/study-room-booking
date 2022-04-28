import json

def main():
    with open('data/rooms.json') as fp:
        data = json.load(fp)  
    for index in range(len(data)):
        room_number = data[index]["room_number"]
        for inside_index in range(len(data[index]["availibility"])):
            availbility = data[index]["availibility"][inside_index]["available"]
            time_slot = data[index]["availibility"][inside_index]["time_slot"]
            booked_by = data[index]["availibility"][inside_index]["booked_by"]
            print(room_number, availbility, time_slot, booked_by)

if __name__ == "__main__":
    main()