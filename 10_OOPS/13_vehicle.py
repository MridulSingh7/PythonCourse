class Engine:
    """Represents a component (Composition) of a Vehicle."""
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        """Returns a string describing the engine."""
        return f"{self.horsepower} HP Engine"

class Vehicle:
    """Represents the base vehicle class."""
    # Class attribute to track the total number of vehicles created
    total_vehicles = 0
    
    def __init__(self, brand, model, engine_horsepower):
        self.brand = brand
        self.model = model
        self._rental_price = 0  # Private attribute for the managed property

        # Composition: Vehicle HAS-A Engine object
        self.engine = Engine(engine_horsepower)
        
        # Update the class attribute whenever a new instance is created
        Vehicle.total_vehicles += 1

    # --- Instance Method ---
    def get_details(self):
        """Returns the brand, model, and engine information."""
        engine_info = self.engine.get_engine_info()
        return f"Brand: {self.brand}, Model: {self.model}, Engine: {engine_info}"

    # --- Static Method (@staticmethod) ---
    @staticmethod
    def get_vehicle_type():
        """Returns a generic type. Does not use self or cls."""
        return "Generic Vehicle"

    # --- Class Method (@classmethod) ---
    @classmethod
    def get_total_vehicles(cls):
        """Returns the total number of vehicles created. Uses the class state (cls.total_vehicles)."""
        return cls.total_vehicles
    
    # --- Property (Getter) ---
    @property
    def rental_price(self):
        """Allows access to the rental price attribute."""
        return self._rental_price

    # --- Property Setter ---
    @rental_price.setter
    def rental_price(self, price):
        """Validates the rental price before assignment."""
        if price < 0:
            raise ValueError("Rental price cannot be negative.")
        self._rental_price = price


class Car(Vehicle):
    """Represents a Car, inheriting from Vehicle."""
    def __init__(self, brand, model, engine_horsepower, seats):
        # Classical Inheritance: Use super() to call the parent's __init__
        super().__init__(brand, model, engine_horsepower)
        self.seats = seats

    # --- Instance Method Override ---
    def get_details(self):
        """Overrides the parent method to include car-specific details (seats)."""
        # Reuse the base functionality using super()
        base_details = super().get_details()
        return f"{base_details}, Seats: {self.seats}"


# Create instances
truck_engine = Engine(300)
truck = Vehicle("Ford", "F-150", 300)
car1 = Car("Toyota", "Camry", 200, 5)

# Set and validate property
try:
    car1.rental_price = 45.99
    # car1.rental_price = -10 # Uncomment to test ValueError
except ValueError as e:
    print(f"Error setting price: {e}")

# 1. Vehicle Details (Inherited and Overridden Methods)
print("\n--- Instance Details ---")
print(f"Truck Details: {truck.get_details()}")
print(f"Car Details (Override): {car1.get_details()}")

# 2. Class Method (Getting total vehicle count)
print("\n--- Class Method Output ---")
print(f"Total vehicles created: {Car.get_total_vehicles()}") # 2

# 3. Static Method (Generic helper)
print("\n--- Static Method Output ---")
print(f"Vehicle Type Check: {Vehicle.get_vehicle_type()}")

# 4. Property Getter
print("\n--- Property Output ---")
print(f"Car Rental Price: ${car1.rental_price}")


'''
Vehicle Rental System
You are designing a Vehicle Rental System that tracks different types of vehicles and their components.


Tasks:

Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".

Create class Vehicle
Attributes: brand, model, and an Engine object.


Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).

Add a method get_details() returning brand, model, and engine info.

Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".

Add @classmethod get_total_vehicles() → returns total number of vehicles.

Add a @property rental_price and corresponding setter that ensures the value is non-negative.-

Create a Car class that inherits from Vehicle.

Add an attribute seats.

Override the get_details() method and use super() to include base details and append "Seats: X".
'''