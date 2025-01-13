import os
import csv

def find_largest_temp_range(input_folder, output_file):
    station_temp_ranges = {}  

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

                    if station_id not in station_temp_ranges:
                        station_temp_ranges[station_id] = {"max": temp, "min": temp}
                    else:
                        station_temp_ranges[station_id]["max"] = max(station_temp_ranges[station_id]["max"], temp)
                        station_temp_ranges[station_id]["min"] = min(station_temp_ranges[station_id]["min"], temp)

    # Calculate the largest temperature range
    largest_range = 0
    stations_with_largest_range = []
    for station, temps in station_temp_ranges.items():
        temp_range = temps["max"] - temps["min"]
        if temp_range > largest_range:
            largest_range = temp_range
            stations_with_largest_range = [station]
        elif temp_range == largest_range:
            stations_with_largest_range.append(station)

    # Save the results to a file
    with open(output_file, "w") as file:
        file.write("Stations with the Largest Temperature Range:\n")
        file.write(f"Largest Range: {largest_range:.2f}\n")
        for station in stations_with_largest_range:
            file.write(f"{station}\n")

# Run the function
input_folder = "temperature_data"
output_file = "largest_temp_range_station.txt"
find_largest_temp_range(input_folder, output_file)
print(f"Stations with the largest temperature range saved to {output_file}.")
