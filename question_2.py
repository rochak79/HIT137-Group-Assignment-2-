"""
1. Calculate the average temperatures for each season across all years. Save the
result to file “average_temp.txt”.

"""
import pandas as pd
import os

def calculate_seasonal_averages_per_year(input_folder, output_file):
    # Define seasons
    seasons = {
        "Summer": [11, 0, 1],  # December, January, February
        "Autumn": [2, 3, 4],   # March, April, May
        "Winter": [5, 6, 7],   # June, July, August
        "Spring": [8, 9, 10],  # September, October, November
    }

    # Open the output file for writing results
    with open(output_file, "w") as f:
        f.write("Yearly Seasonal Averages Report\n")
        f.write("=" * 50 + "\n\n")
        
        # Iterate through all CSV files
        for file_name in sorted(os.listdir(input_folder)):  # Sorted for year-wise order
            if file_name.endswith(".csv"):
                # Extracting the year from the file name 
                year = file_name.split("_")[-1].split(".")[0]

                # Read the CSV file
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)

                # Write the year heading
                f.write(f"Year: {year}\n")
                f.write("-" * 50 + "\n")

                # Calculate seasonal averages for the year
                for season, months in seasons.items():
                    # Select the corresponding month columns
                    month_indices = [4 + m for m in months]
                    season_data = data.iloc[:, month_indices]
                    season_avg = season_data.mean().mean()  # Average temperature for the season

                    # Write the season result
                    f.write(f"{season:<10}: {season_avg:.2f} \n")

                # Add a blank line after each year
                f.write("\n")

# Input and output file paths
input_folder = "temperature_data"
output_file = "average_temp.txt"

# Run the function
calculate_seasonal_averages_per_year(input_folder, output_file)
print(f"Seasonal averages saved to {output_file}.")


"""
2. Find Station with Largest Temperature Range
python
Copy code
"""
def find_largest_temp_range(input_folder, output_file):
    # Create variables to track the largest temperature range and corresponding stations
    largest_range = float('-inf')
    largest_range_stations = []
    largest_range_file = None

    # Process each file in the input folder
    for file_name in sorted(os.listdir(input_folder)):  # Process files in sorted order
        if file_name.endswith(".csv"):
            # Read the CSV file
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)

            # Calculate temperature range (max - min) for each station
            # Assuming temperature data starts from the 5th column onward
            station_ranges = data.iloc[:, 4:].max(axis=1) - data.iloc[:, 4:].min(axis=1)

            # Find the maximum temperature range in the current file
            max_range = station_ranges.max()

            # If this file has a larger range, update the tracking variables
            if max_range > largest_range:
                largest_range = max_range
                largest_range_stations = data.loc[station_ranges == max_range, "STATION_NAME"].tolist()
                largest_range_file = file_name

    # Write the results to the output file
    with open(output_file, "w") as f:
        f.write("Stations with the Largest Temperature Range\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Largest Temperature Range: {largest_range:.2f} \n")
        f.write(f"File: {largest_range_file}\n")
        f.write("Station(s):\n")
        for station in largest_range_stations:
            f.write(f"  - {station}\n")
        f.write("\n")

# Input folder containing the temperature CSV files
input_folder = "temperature_data"

# Output file where the results will be saved
output_file = "largest_temp_range_station.txt"

# Call the function
find_largest_temp_range(input_folder, output_file)

print(f"Results saved to {output_file}.")


# Function to find the station(s) with the largest temperature range
def find_largest_temp_range_by_year(input_folder, output_folder):
    for file_name in sorted(os.listdir(input_folder)):  # Process files in sorted order
        if file_name.endswith(".csv"):
            # Extract the year from the file name
            year = file_name.split("_")[-1].split(".")[0]

            # Read the CSV file
            file_path = os.path.join(input_folder, file_name)
            data = pd.read_csv(file_path)

            # Calculate temperature range (max - min) for each station
            station_ranges = data.iloc[:, 4:].max(axis=1) - data.iloc[:, 4:].min(axis=1)

            # Find the largest temperature range in the file
            largest_range = station_ranges.max()
            largest_range_stations = data.loc[station_ranges == largest_range, "STATION_NAME"].tolist()

            # Write the results to the output file
            output_file = os.path.join(output_folder, f"largest_temp_range_{year}.txt")
            with open(output_file, "w") as f:
                f.write(f"Largest Temperature Range for Year {year}\n")
                f.write("=" * 70 + "\n\n")
                f.write(f"Largest Temperature Range: {largest_range:.2f} \n")
                f.write("Station(s):\n")
                for station in largest_range_stations:
                    f.write(f"  - {station}\n")

    print(f"Largest temperature range results saved to {output_folder}.")



def find_largest_temp_range(input_folder, output_file):
    with open(output_file, "w") as f:
        f.write("Stations with the Largest Temperature Range\n")
        f.write("=" * 70 + "\n\n")
        
        for file_name in sorted(os.listdir(input_folder)):
            if file_name.endswith(".csv"):
                year = file_name.split("_")[-1].split(".")[0]
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)
                
                # Calculate temperature range (max - min) for each station
                station_ranges = data.iloc[:, 4:].max(axis=1) - data.iloc[:, 4:].min(axis=1)
                max_range = station_ranges.max()
                largest_range_stations = data.loc[station_ranges == max_range, "STATION_NAME"].tolist()
                
                f.write(f"Year: {year}\n")
                f.write(f"Largest Temperature Range: {max_range:.2f} C\n")
                f.write("Station(s):\n")
                for station in largest_range_stations:
                    f.write(f"  - {station}\n")
                f.write("\n")
"""
3, Find the warmest and coolest station/stations. Save the result to file
“warmest_and_coolest_station.txt”

"""
# Function to find the warmest and coolest stations
def find_warmest_and_coolest_stations(input_folder, output_file):
    with open(output_file, "w") as f:
        f.write("Warmest and Coolest Stations\n")
        f.write("=" * 70 + "\n\n")
        
        for file_name in sorted(os.listdir(input_folder)):
            if file_name.endswith(".csv"):
                year = file_name.split("_")[-1].split(".")[0]
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)
                
                # Calculate average temperature for each station
                station_avg_temps = data.iloc[:, 4:].mean(axis=1)
                max_avg_temp = station_avg_temps.max()
                min_avg_temp = station_avg_temps.min()
                warmest_stations = data.loc[station_avg_temps == max_avg_temp, "STATION_NAME"].tolist()
                coolest_stations = data.loc[station_avg_temps == min_avg_temp, "STATION_NAME"].tolist()
                
                f.write(f"Year: {year}\n")
                f.write(f"Warmest Temperature: {max_avg_temp:.2f} °C\n")
                f.write("Warmest Station(s):\n")
                for station in warmest_stations:
                    f.write(f"  - {station}\n")
                f.write(f"Coolest Temperature: {min_avg_temp:.2f} °C\n")
                f.write("Coolest Station(s):\n")
                for station in coolest_stations:
                    f.write(f"  - {station}\n")
                f.write("\n")

# Define input and output paths
input_folder = "temperature_data"
output_file_largest_range = "largest_temp_range_station.txt"
output_file_warmest_coolest = "warmest_and_coolest_station.txt"

# Run the functions
find_largest_temp_range(input_folder, output_file_largest_range)
find_warmest_and_coolest_stations(input_folder, output_file_warmest_coolest)

print(f"Largest temperature range results saved to {output_file_largest_range}.")
print(f"Warmest and coolest station results saved to {output_file_warmest_coolest}.")