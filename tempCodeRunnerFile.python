import math

class Planet:
    def __init__(self, name, planet_type, star):
        # Data Validation
        if not all(isinstance(arg, str) for arg in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        if not all(arg.strip() for arg in [name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"

class SolarSystem:
    def __init__(self, system_name):
        self.system_name = system_name
        self.planets = []

    def add_planet(self, planet_instance):
        if isinstance(planet_instance, Planet):
            self.planets.append(planet_instance)
        else:
            raise TypeError("Only Planet objects can be added to the SolarSystem.")

    def show_all_planets(self):
        print(f"\n--- Surveying the {self.system_name} System ---")
        if not self.planets:
            print("No planets in this system yet.")
        for p in self.planets:
            print(p)

# --- Execution Block ---
if __name__ == "__main__":
    try:
        # Create the Manager
        milky_way = SolarSystem("The Milky Way")

        # Create the Objects
        earth = Planet("Earth", "Terrestrial", "Sun")
        jupiter = Planet("Jupiter", "Gas Giant", "Sun")
        kepler = Planet("Kepler-22b", "Exoplanet", "Kepler-22")

        # Add them to the system
        milky_way.add_planet(earth)
        milky_way.add_planet(jupiter)
        milky_way.add_planet(kepler)

        # Output results
        milky_way.show_all_planets()
        print(f"\nExample Action: {earth.orbit()}")

    except (TypeError, ValueError) as e:
        print(f"Configuration Error: {e}")