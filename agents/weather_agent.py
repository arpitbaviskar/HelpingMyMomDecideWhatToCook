def get_weather_tags(weather_input):
    if weather_input == "hot":
        return ["hot", "any"]
    elif weather_input == "cold":
        return ["cold", "any"]
    elif weather_input == "rainy":
        return ["rainy", "any"]
    else:
        return ["any"]
