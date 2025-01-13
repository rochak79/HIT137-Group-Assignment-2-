import os
import csv
def find_warmest_and_coolest_stations(input_folder, output_file):
    station_temps = {}  

    # Process each file in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        if file_name.endswith(".csv"):
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)  

                for row in reader:
                    station_id = row[0]  
                    temp = float(row[2]) 

                    if station_id not in station_temps:
                        station_temps[station_id] = {"total": temp, "count": 1}
                    else:
                        station_temps[station_id]["total"] += temp
                        station_temps[station_id]["count"] += 1

    # Calculate the average temperatures
    station_avg_temps = {
        station: temps["total"] / temps["count"] for station, temps in station_temps.items()
    }

    # Find the warmest and coolest stations
    max_avg_temp = max(station_avg_temps.values())
    min_avg_temp = min(station_avg_temps.values())

    warmest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == max_avg_temp]
    coolest_stations = [station for station, avg_temp in station_avg_temps.items() if avg_temp == min_avg_temp]

    # Save the results to a file
    with open(output_file, "w") as file:
        file.write("Warmest and Coolest Stations:\n")
        file.write(f"Warmest Temperature: {max_avg_temp:.2f}\n")
        for station in warmest_stations:
            file.write(f"Warmest Station: {station}\n")
        file.write(f"Coolest Temperature: {min_avg_temp:.2f}\n")
        for station in coolest_stations:
            file.write(f"Coolest Station: {station}\n")

# Run the function
input_folder = "temperature_data"
output_file = "warmest_and_coolest_station.txt"
find_warmest_and_coolest_stations(input_folder, output_file)
print(f"Warmest and coolest stations saved to {output_file}.")
