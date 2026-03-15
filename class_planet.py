class Planet:
    def __init__(self, name, planet_type, star):
        # Check that all arguments are strings
        if not all(isinstance(arg, str) for arg in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        
        # Check that none of the strings are empty or just whitespace
        if not all(arg.strip() for arg in [name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        # Assign attributes
        self.name = name
        self.planet_type = planet_type
        self.star = star

    def orbit(self):
        return f"{self.name} is orbiting around {self.star}"

    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# Create planets and store them in a list
planets = [
    Planet("Earth", "Terrestrial", "Sun"),
    Planet("Jupiter", "Gas Giant", "Sun"),
    Planet("Kepler-22b", "Exoplanet", "Kepler-22")
]

# Loop through planets and print details
for planet in planets:
    print(planet)        # __str__ output
    print(planet.orbit())  # orbit method output
    print()  # blank line for readability
