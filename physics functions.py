def calculate_distance(speed, time):
    """Calculate distance traveled."""
    return speed * time

def calculate_speed(distance, time):
    """Calculate speed."""
    if time == 0:
        raise ValueError("Time cannot be zero.")
    return distance / time

def calculate_force(mass, acceleration):
    """Calculate force using Newton's second law."""
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    """Calculate kinetic energy."""
    return 0.5 * mass * velocity ** 2

def calculate_potential_energy(mass, height, gravity=9.81):
    """Calculate gravitational potential energy."""
    return mass * gravity * height

# Example values for calculations
speed = 10  # m/s
time = 5    # s
distance = 50  # m
mass = 2    # kg
acceleration = 9.81  # m/s^2
velocity = 3  # m/s
height = 5   # m

# Perform calculations
distance_traveled = calculate_distance(speed, time)
calculated_speed = calculate_speed(distance, time)
force = calculate_force(mass, acceleration)
kinetic_energy = calculate_kinetic_energy(mass, velocity)
potential_energy = calculate_potential_energy(mass, height)

# Print results
print(f"1. Distance traveled: {distance_traveled:.2f} m")
print(f"2. Speed: {calculated_speed:.2f} m/s")
print(f"3. Force: {force:.2f} N")
print(f"4. Kinetic Energy: {kinetic_energy:.2f} J")
print(f"5. Potential Energy: {potential_energy:.2f} J")