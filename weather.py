# Weather Data Analyzer with User Input

# Function to calculate average of a list
def calculate_average(data):
    return sum(data) / len(data)

# Function to determine weather condition
def determine_weather_condition(temp, humidity):
    if temp > 32 and humidity < 60:
        return "Sunny"
    elif temp < 30 and humidity > 70:
        return "Rainy"
    elif 30 <= temp <= 32 and 60 <= humidity <= 70:
        return "Cloudy"
    else:
        return "Moderate"

# Input from user
days = int(input("Enter number of days to analyze: "))
temperature_data = []
humidity_data = []

for i in range(days):
    temp = float(input(f"Enter temperature for day {i + 1} (°C): "))
    humidity = float(input(f"Enter humidity for day {i + 1} (%): "))
    temperature_data.append(temp)
    humidity_data.append(humidity)

# Calculate averages
avg_temp = calculate_average(temperature_data)
avg_humidity = calculate_average(humidity_data)

# Display results
print("\n=== Weather Data Analyzer Results ===")
print(f"Average Temperature: {avg_temp:.2f}°C")
print(f"Average Humidity: {avg_humidity:.2f}%")
print(f"Overall Weather Condition: {determine_weather_condition(avg_temp, avg_humidity)}")