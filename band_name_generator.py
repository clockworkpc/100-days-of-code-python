def generate_band_name():
    city = input("What is the name of your city? ")
    pet = input("What is the name of your pet? ")
    return f"Your band could be {city} {pet}"


welcome = "Welcome to the Band Name Generator."
print(welcome)
print(generate_band_name())
