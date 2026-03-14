import math

class Planet:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass     # in kg
        self.radius = radius # in meters

    def get_volume(self):
        # Formula for volume of a sphere: (4/3) * pi * r^3
        volume = (4/3) * math.pi * (self.radius ** 3)
        return volume

    def get_density(self):
        # --- YOUR CODE HERE ---
        # 1. Get the volume using self.get_volume()
        volume = self.get_volume()
        mass = self.mass
        # 2. Return mass divided by volume
        density = mass / volume
        return density

# Test it out!
# Keep your class up here...

if __name__ == "__main__":
    # Everything inside here only runs if you run THIS file directly
    earth = Planet("Earth", 5.97e24, 6371000)
    print(f"{earth.name} Density: {earth.get_density():.2f} kg/m^3")
