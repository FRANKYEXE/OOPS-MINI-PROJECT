# # Scenario: A cinema hall wants a simple ticket booking system using Python.
# How would you store available and booked seats using lists or dictionaries?
# How would you ensure a seat is not booked twice?
# How would you allow users to cancel a booked seat?


class CinemaHall:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = {seat: True for seat in range(1, total_seats + 1)}
        self.booked_seats = {}

    def book_seat(self, seat_number):
        if seat_number in self.available_seats and self.available_seats[seat_number]:
            self.available_seats[seat_number] = False
            self.booked_seats[seat_number] = True
            print(f"Seat {seat_number} has been successfully booked.")
        else:
            print(f"Seat {seat_number} is already booked or does not exist.")

    def cancel_seat(self, seat_number):
        if seat_number in self.booked_seats and self.booked_seats[seat_number]:
            self.booked_seats[seat_number] = False
            self.available_seats[seat_number] = True
            print(f"Seat {seat_number} has been successfully canceled.")
        else:
            print(f"Seat {seat_number} is not booked or does not exist.")

    def display_seats(self):
        print("Available seats:", [seat for seat, available in self.available_seats.items() if available])
        print("Booked seats:", [seat for seat, booked in self.booked_seats.items() if booked])

if __name__ == "__main__":
    cinema_hall = CinemaHall(10)
    cinema_hall.display_seats()
    cinema_hall.book_seat(3)
    cinema_hall.book_seat(3)
    cinema_hall.display_seats()
    cinema_hall.cancel_seat(3)
    cinema_hall.display_seats()