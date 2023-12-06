# from datetime import datetime


class Package:  # Class for package
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, notes):
        self.package_id = package_id  # Initializes package attributes
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes
        self.depart_time = None  # Departure time set to none initially
        self.delivery_time = None  # Delivery time set to none initially
        # self.status = "At Hub"  # For Nearest_Neighbor_Status class
        # self.hash_key = package_id  # For Nearest_Neighbor_Status class

    def set_depart_time(self, time):  # Sets the departure time of the packages
        self.depart_time = time

    def set_delivery_time(self, time):  # Sets the delivery time of the packages
        self.delivery_time = time

    # Comment out block is used for the test print to visualize the algorithm working in truck.py
    '''def Nearest_Neighbor_Status(self, user_time): 
        if not self.delivery_time or not self.depart_time:
            return "Times not set"

        # Convert self.delivery_time to datetime object if it's not
        if isinstance(self.delivery_time, str):
            self.delivery_time = datetime.strptime(self.delivery_time, '%Y-%m-%d %H:%M:%S')

        if isinstance(self.depart_time, str):
            self.depart_time = datetime.strptime(self.depart_time, '%Y-%m-%d %H:%M:%S')

        if user_time < self.delivery_time:
            return "In Transit"
        elif user_time == self.delivery_time:
            return "Out for Delivery"
        else:
            return "Delivered"'''
