class User:
    def __init__(self, user_id, name, contact_details):
        self.user_id = user_id
        self.name = name
        self.contact_details = contact_details
        

class Host(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.properties = []

    def list_property(self, property):
        self.properties.append(property)

    def display(self):
        print(f"{self.user_id}, {self.name}, {self.contact_details}")

class Guest(User):
    def __init__(self, user_id, name, contact_details):
        super().__init__(user_id, name, contact_details)
        self.bookings = []

    def display(self):
        print(f"{self.user_id}, {self.name}, {self.contact_details}")


    def book_property(self, property, checkInDate, checkOut):
        if property.availability:
            booking = Booking(len(self.bookings) + 1, property, self, checkInDate, checkOut)
            self.bookings.append(booking)
            property.availability = False
            return booking
        else:
            return None
        


class Property:
    def __init__(self, property_id, name, location, description, ChargesPerNight):
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.ChargesPerNight = ChargesPerNight
        self.availability = True
        
    def display(self):
        print(f"{self.property_id}, {self.name}, {self.location}, {self.description}, {self.ChargesPerNight}")

        
    def available(self, checkInDate, checkOut):
        for booked_date in self.booked:
            if not (checkOut <= booked_date[0] or checkInDate >= booked_date[1]):
                return False
        return True

    def update_availability(self, checkInDate, checkOut, available):
        if available:
            self.booked = [date for date in self.booked if not (checkInDate <= date[1] and checkOut >= date[0])]
        else:
            self.booked.append((checkInDate, checkOut))


class Booking:
    def __init__(self, booking_id, property, guest, checkInDate, checkOut, status='confirmed'):
        self.booking_id = booking_id
        self.property = property
        self.guest = guest
        self.checkInDate = checkInDate
        self.checkOut = checkOut
        self.status = status

    def cancel_booking(self):
        self.status = 'canceled'
        self.property.availability = True

class Review:
    def __init__(self, review_id, booking, rating, comment):
        self.review_id = review_id
        self.booking = booking
        self.rating = rating
        self.comment = comment

    def add_review(self, rating, comment):
        self.rating = rating
        self.comment = comment
        print(f"Review added: Rating - {rating}, Comment - '{comment}'")



host1 = Host(1, "Faris Ch", "faris@gmail.com")
host1.display()
guest1 = Guest(101, "Ali Khan", "ali@gmail.com")
guest1.display()
property1 = Property(2, "Beach House", "Beachfront", "Beautiful beach house view", 20000)
property1.display()

booking1 = guest1.book_property(property1, "2024-07-01", "2024-07-05")
review1 = Review(1, booking1, 5, "Excellent property, highly recommended!")
review1.add_review(5, "Excellent property, highly recommended!")