import sys
import uuid
from datetime import datetime

# Class to manage individual itineraries (transport, accommodation, and activities)
class Itinerary:
    def __init__(self, transport, accommodation, activities=None):
        self.transport = transport
        self.accommodation = accommodation
        self.activities = activities if activities else []

    def display_itinerary(self):
        print(f"Transport: {self.transport}")
        print(f"Accommodation: {self.accommodation}")
        print(f"Activities: {', '.join(self.activities) if self.activities else 'None'}")

# Class to manage bookings
class Booking:
    def __init__(self, booking_id, customer_name, travel_date, destination, itinerary=None):
        self.booking_id = booking_id  # User-defined booking ID
        self.customer_name = customer_name
        self.travel_date = travel_date  # Storing date in DD-MM-YYYY format
        self.destination = destination
        self.itinerary = itinerary if itinerary else Itinerary("", "")

    def display_booking(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer: {self.customer_name}")
        print(f"Travel Date: {self.travel_date}")
        print(f"Destination: {self.destination}")
        print("Itinerary:")
        self.itinerary.display_itinerary()

# Class to generate invoices
class Invoice:
    def __init__(self, booking, transport_cost, accommodation_cost, activity_costs=None):
        self.booking = booking
        self.transport_cost = transport_cost
        self.accommodation_cost = accommodation_cost
        self.activity_costs = activity_costs if activity_costs else []

    def calculate_total(self):
        activity_total = sum(self.activity_costs)
        total_cost = self.transport_cost + self.accommodation_cost + activity_total
        return total_cost

    def generate_invoice(self):
        total_cost = self.calculate_total()
        invoice = f"--- Invoice ---\n"
        invoice += f"Customer: {self.booking.customer_name}\n"
        invoice += f"Destination: {self.booking.destination}\n"
        invoice += f"Travel Date: {self.booking.travel_date}\n"
        invoice += f"Transport Cost: ${self.transport_cost}\n"
        invoice += f"Accommodation Cost: ${self.accommodation_cost}\n"
        invoice += f"Activity Costs: ${', '.join(map(str, self.activity_costs))} (Total: ${sum(self.activity_costs)})\n"
        invoice += f"Total: ${total_cost}\n"
        return invoice

# List to store all bookings
bookings = []

# Helper function to convert date formats
def format_date(date_string):
    try:
        # Convert from DD-MM-YYYY to standard format and back
        date_obj = datetime.strptime(date_string, "%d-%m-%Y")
        return date_obj.strftime("%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use DD-MM-YYYY.")
        return None

# Function to create a booking
def create_booking():
    customer_name = input("Enter customer name: ")
    travel_date = input("Enter travel date (DD-MM-YYYY): ")
    travel_date = format_date(travel_date)
    if not travel_date:
        return
    destination = input("Enter destination: ")
    booking_id = input("Enter your preferred Booking ID (leave blank to auto-generate): ")

    if not booking_id:
        # Fallback to auto-generated UUID if no preferred ID is provided
        booking_id = str(uuid.uuid4())

    transport = input("Enter transport details: ")
    accommodation = input("Enter accommodation details: ")
    activities = input("Enter activities (comma-separated): ").split(",")
    itinerary = Itinerary(transport, accommodation, activities)
    booking = Booking(booking_id, customer_name, travel_date, destination, itinerary)
    bookings.append(booking)
    print(f"Booking created with ID: {booking.booking_id}")

# Function to read/display a booking
def read_booking():
    booking_id = input("Enter booking ID: ")
    for booking in bookings:
        if booking.booking_id == booking_id:
            booking.display_booking()
            return
    print(f"Booking with ID {booking_id} not found.")

# Function to update a booking
def update_booking():
    booking_id = input("Enter booking ID: ")
    for booking in bookings:
        if booking.booking_id == booking_id:
            customer_name = input("Enter new customer name (leave blank to keep current): ")
            travel_date = input("Enter new travel date (DD-MM-YYYY) (leave blank to keep current): ")
            destination = input("Enter new destination (leave blank to keep current): ")
            if customer_name:
                booking.customer_name = customer_name
            if travel_date:
                travel_date = format_date(travel_date)
                if travel_date:
                    booking.travel_date = travel_date
            if destination:
                booking.destination = destination
            print(f"Booking with ID {booking_id} updated.")
            return
    print(f"Booking with ID {booking_id} not found.")

# Function to delete a booking
def delete_booking():
    booking_id = input("Enter booking ID: ")
    global bookings
    bookings = [booking for booking in bookings if booking.booking_id != booking_id]
    print(f"Booking with ID {booking_id} deleted.")

# Function to generate an invoice
def generate_invoice():
    booking_id = input("Enter booking ID: ")
    for booking in bookings:
        if booking.booking_id == booking_id:
            transport_cost = float(input("Enter transport cost: "))
            accommodation_cost = float(input("Enter accommodation cost: "))
            activity_costs = list(map(float, input("Enter activity costs (comma-separated): ").split(",")))
            invoice = Invoice(booking, transport_cost, accommodation_cost, activity_costs)
            print("\n--- Invoice ---")
            print(invoice.generate_invoice())
            return
    print(f"Booking with ID {booking_id} not found.")

# Main function to run the booking system
def main():
    while True:
        print("\n--- Travel Booking System ---")
        print("1. Create Booking")
        print("2. Read Booking")
        print("3. Update Booking")
        print("4. Delete Booking")
        print("5. Generate Invoice")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_booking()
        elif choice == '2':
            read_booking()
        elif choice == '3':
            update_booking()
        elif choice == '4':
            delete_booking()
        elif choice == '5':
            generate_invoice()
        elif choice == '6':
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
