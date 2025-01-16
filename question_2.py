"""
Question 2
Create a program that analyses temperature data collected from multiple weather
stations in Australia. The data is stored in multiple CSV files under a temperatures
folder, with each file representing data from one year.

You need to:

1.Calculate the average temperatures for each season across all years. Save the
result to file “average_temp.txt”.
2. Find the station/stations have the largest temperature range. Save the result to
file “largest_temp_range_station.txt”.
3. Find the warmest and coolest station/stations. Save the result to file
“warmest_and_coolest_station.txt”.
"""



import pandas as pd
import os

"""
1. Calculate the average temperatures for each season across all years. Save the
result to file “average_temp.txt”.

"""

def calculate_seasonal_averages_per_year(input_folder, output_file):
    # Defining seasons
    seasons = {
        "Summer": [11, 0, 1],  # December, January, February 
        # [i.e, total average from the indivual averages of december, january, february combined][
        # excel==AVERAGE(P2:P113,E2:E113,F2:F113)]
        "Autumn": [2, 3, 4],   # March, April, May
        "Winter": [5, 6, 7],   # June, July, August
        "Spring": [8, 9, 10],  # September, October, November
    }

    # Opening up the output file for writing results
    with open(output_file, "w") as f:
        f.write("Yearly Seasonal Averages Report\n")
        f.write("=" * 50 + "\n\n")
        
        # Iterating through all CSV files
        for file_name in sorted(os.listdir(input_folder)):  # Sorting it in year-wise order
            if file_name.endswith(".csv"):
                # Extracting the year from the file name 
                year = file_name.split("_")[-1].split(".")[0]

                # Reading through the CSV file
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)

                # Writing the year heading
                f.write(f"Year: {year}\n")
                f.write("-" * 50 + "\n")

                # Calculating seasonal averages for the year
                for season, months in seasons.items():
                    # Select the corresponding month columns
                    month_indices = [4 + m for m in months]
                    season_data = data.iloc[:, month_indices]
                    season_avg = season_data.mean().mean()  # calculating averages of temperature for each season

                    # Writing the season result
                    f.write(f"{season:<10}: {season_avg:.2f} \n")

                # Adding a blank line after each year
                f.write("\n")

# Input and output paths
input_folder = "temperature_data"
output_file = "average_temp.txt"

# Running the functions
calculate_seasonal_averages_per_year(input_folder, output_file)
print(f"Seasonal averages saved to {output_file}.")


"""
2. Find the station/stations have the largest temperature range. Save the result to
file “largest_temp_range_station.txt”

"""

def find_largest_temp_range(input_folder, output_file):
    """
    Finding the warmest and coolest temperatures and their respective stations for each year
    across multiple CSV files and calculating the overall largest temperature range.
    Hence, saving the resulting text file.
    """
    # Storing overall data for later 
    overall_data = {
        "largest_range": float('-inf'),
        "warmest_temp": None,
        "warmest_stations": [],
        "coolest_temp": None,
        "coolest_stations": [],
        "year": None
    }

    # Opening the output file for writing
    with open(output_file, "w") as f:
        f.write("Stations with the Largest Temperature Range\n")
        f.write("=" * 70 + "\n\n")
        
        # Processing all files in the folder
        for file_name in sorted(os.listdir(input_folder)):  # Ensuring files are processed in order
            if file_name.endswith(".csv"):
                # Extracting the year from the file name
                try:
                    year = file_name.split("_")[-1].split(".")[0]
                except IndexError:
                    year = "Unknown"
                
                # Loading the CSV file
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)

                # Ensuring columns are numeric and exclude non-temperature columns
                temperature_columns = data.columns[4:]  # assumptions as temperature data starts from 5th column
                data[temperature_columns] = data[temperature_columns].apply(pd.to_numeric, errors='coerce')

                # Finding the warmest and coolest temperatures annually
                warmest_temperature = data[temperature_columns].max().max()
                coolest_temperature = data[temperature_columns].min().min()

                # Finding the stations with the warmest and coolest temperatures
                warmest_stations = data.loc[data[temperature_columns].max(axis=1) == warmest_temperature, "STATION_NAME"].tolist()
                coolest_stations = data.loc[data[temperature_columns].min(axis=1) == coolest_temperature, "STATION_NAME"].tolist()

                # Calculating the temperature range for the year
                temp_range = warmest_temperature - coolest_temperature

                # Writing yearly results to the output file
                f.write(f"Year: {year}\n")
                f.write(f"Warmest Temperature: {warmest_temperature:.2f} \n")
                f.write("Warmest Station  :\n")
                for station in warmest_stations:
                    f.write(f"  - {station}\n")
                f.write(f"Coolest Temperature: {coolest_temperature:.2f} \n")
                f.write("Coolest Station  :\n")
                for station in coolest_stations:
                    f.write(f"  - {station}\n")
                f.write(f"Temperature Range: {temp_range:.2f} \n\n")
                
                # if necessary, updating the overall largest range as well
                if temp_range > overall_data["largest_range"]:
                    overall_data["largest_range"] = temp_range
                    overall_data["warmest_temp"] = warmest_temperature
                    overall_data["warmest_stations"] = warmest_stations
                    overall_data["coolest_temp"] = coolest_temperature
                    overall_data["coolest_stations"] = coolest_stations
                    overall_data["year"] = year

        # Writing overall results to the output file
        f.write("Overall Station   with the Largest Temperature Range\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Largest Temperature Range: {overall_data['largest_range']:.2f} \n")
        f.write(f"Year: {overall_data['year']}\n")
        f.write(f"Warmest Temperature: {overall_data['warmest_temp']:.2f} \n")
        f.write("Warmest Station  :\n")
        for station in overall_data["warmest_stations"]:
            f.write(f"  - {station}\n")
        f.write(f"Coolest Temperature: {overall_data['coolest_temp']:.2f} \n")
        f.write("Coolest Station  :\n")
        for station in overall_data["coolest_stations"]:
            f.write(f"  - {station}\n")
    
    print(f"Results saved to {output_file}.")

# Assigning temperature data in input_folder variable 
input_folder = "temperature_data"  # Replacing with the correct folder path

# Outputs for all results
output_file = "largest_temp_range_station.txt"

# Calling the function
find_largest_temp_range(input_folder, output_file)

"""
3, Find the warmest and coolest station/stations. Save the result to file
“warmest_and_coolest_station.txt”

"""

# Function to find warmest and coolest stations (with overall calculations)
def find_warmest_and_coolest_stations(input_folder, output_file):
    # Initializing variables to track overall warmest and coolest temperatures and stations
    overall_warmest_temp = float('-inf')
    overall_coolest_temp = float('inf')
    overall_warmest_stations = []
    overall_coolest_stations = []
    warmest_year = None
    coolest_year = None

    # Opening the output file to write results
    with open(output_file, "w") as f:
        f.write("Warmest and Coolest Stations\n")
        f.write("=" * 70 + "\n\n")

        # Processing each file in the input folder
        for file_name in sorted(os.listdir(input_folder)):  # Processing files in sorted order
            if file_name.endswith(".csv"):
                year = file_name.split("_")[-1].split(".")[0]
                file_path = os.path.join(input_folder, file_name)
                data = pd.read_csv(file_path)

                # Calculating average temperatures for each stations
                station_max_temps = data.iloc[:, 4:].max(axis=1)
                station_min_temps = data.iloc[:, 4:].min(axis=1)
                max_temp = station_max_temps.max()
                min_temp = station_min_temps.min()
                warmest_stations = data.loc[station_max_temps == max_temp, "STATION_NAME"].tolist()
                coolest_stations = data.loc[station_min_temps == min_temp, "STATION_NAME"].tolist()

                # Writing yearly results to the file
                f.write(f"Year: {year}\n")
                f.write(f"Warmest Temperature: {max_temp:.2f} \n")
                f.write("Warmest Station  :\n")
                for station in warmest_stations:
                    f.write(f"  - {station}\n")
                f.write(f"Coolest Temperature: {min_temp:.2f} \n")
                f.write("Coolest Station  :\n")
                for station in coolest_stations:
                    f.write(f"  - {station}\n")
                f.write("\n")

                # Updating overall warmest and coolest stations and temperatures
                if max_temp > overall_warmest_temp:
                    overall_warmest_temp = max_temp
                    overall_warmest_stations = warmest_stations
                    warmest_year = year

                if min_temp < overall_coolest_temp:
                    overall_coolest_temp = min_temp
                    overall_coolest_stations = coolest_stations
                    coolest_year = year

        # Writing overall results to the file
        f.write("Overall Warmest and Coolest Stations\n")
        f.write("=" * 70 + "\n\n")
        f.write(f"Warmest Temperature: {overall_warmest_temp:.2f} \n")
        f.write(f"Year: {warmest_year}\n")
        f.write("Warmest Station  :\n")
        for station in overall_warmest_stations:
            f.write(f"  - {station}\n")
        f.write(f"\nCoolest Temperature: {overall_coolest_temp:.2f} \n")
        f.write(f"Year: {coolest_year}\n")
        f.write("Coolest Station  :\n")
        for station in overall_coolest_stations:
            f.write(f"  - {station}\n")

    print(f"All results saved to {output_file}.")

# Defining input and output paths
input_folder = "temperature_data"
output_file_warmest_coolest = "warmest_and_coolest_station.txt"

# Running the function
find_warmest_and_coolest_stations(input_folder, output_file_warmest_coolest)
